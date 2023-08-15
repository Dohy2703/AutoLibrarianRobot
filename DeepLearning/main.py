import time
import cv2
import numpy as np
from detect_book import Operator
# from TCPmanager import TCP
from collections import defaultdict
from ultralytics import YOLO
from realsense import Realsense
from detect_book import DetectBook


realsense = True  # 지역변수 오류때문에 미리 선언해둠
'''로봇의 state 정의'''
# status = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
status = None
wait = False
find_word = 623576 #623400 # 625223 # 623400

if __name__ == '__main__':
    kdh = True
    ChadChang = False

    if kdh:
        model = YOLO('/home/kdh/Downloads/best_v8.pt')
        book_detector = DetectBook(0)
        realsense = True  # True면 뎁스카메라, False면 비디오
    elif ChadChang:
        # runner = Operator()  '''state마다 동작을 정해주는 클래스를 따로 만들음'''
        calb_path = '/home/chad-chang/PycharmProjects/23_HF071/calib_data/MultiMatrix.npz'
        model = YOLO('/home/chad-chang/PycharmProjects/23_HF071/best.pt')
        book_detector = DetectBook(calb_path)
        realsense = True  # True면 뎁스카메라, False면 비디오
        tcp = TCP('127.0.1.1', 2016, available = False)

    # Flags
    tracking = False  # 글자 읽었을 때 트래킹
    detect_center_book = True   # 말 그대로 중앙에 있는 책을 계속 검출할 것인지.

    if realsense:
        RS = Realsense()
    else:  # video
        cap = cv2.VideoCapture('/home/kdh/Downloads/20230801_002342.mp4')

    # Lists
    track_history = defaultdict(lambda: [])

    frame = []
    book_id = 0
    label_id = 0

    # Loop through the video frames
    while True:
        starttime = time.time()
        if realsense:
            results = model.track(RS.color_image, persist=True) # Run YOLOv8 tracking on the frame, persisting tracks between frames
            book_detector.get_image(RS)
        else:  # video
            _, frame = cap.read()
            frame = cv2.resize(frame, (640, 384))
            results = model.track(frame, persist=True)
            book_detector.get_video_image(frame)

            '''통신값 받기 대기'''

        '''status0 : 통신 대기'''
        if status == 0:
            status_buff = tcp.receive()  # 통신받은 값은 값은 status값임
            if status_buff:
                status = status_buff
            print(status)

            '''status1 : 책 읽으러 동작''' # 조금 수정할 필요있을듯
        elif status == 1:  # 책 읽으러 동작
            if not wait:
                ret_r = runner.run1(book_detector, results, visual = True)
                print(ret_r)
                print(runner.TF)
                # 보내는 값이 온전한지 확인
                # 통신 보내는 것필요
                if runner.TF.shape == (4,4): # 유효성이 검증되면
                    tcp.send(runner.TF)
                wait = True
            status_buff = tcp.receive()
            if status_buff:
                status = status_buff
                wait = False

            '''status2 : 글자 읽기 '''
        elif status == 2:  # reading by ocr
            ret_r = runner.run2(book_detector, results,623480)
            # print(ret_r)
            if ret_r:
                status = 3
                # print('status', status)
            else:
                status = 8
                # print('status =', status)
            '''status3: 해당 책 위치로 이동'''
        elif status == 3:  # 해당책 위치로 이동
            ret_r = runner.run3(book_detector, results)


        # 트래킹
        if results[0].boxes != None and results[0].boxes.id != None:
            annotated_frame = results[0].plot()  # Visualize the results on the frame

            if tracking:  # w 누르고 글자를 읽기 성공 시 트래킹
                book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)  # 마스크 검출
                label_id, book_id, label_idx, book_idx = book_detector.IDcheck(label_id, book_id)
                if label_id==-1 and book_id==-1:
                    tracking=False
                else:
                    book_detector.tracking_getter(label_idx, book_idx, visualize=True)  # 글자 읽은 책, 글자 읽은 라벨지, 책+라벨지 트래킹

            cv2.imshow("YOLOv8 Tracking", annotated_frame)
        else:  # not tracking
            cv2.imshow("YOLOv8 Tracking", results[0].plot())

        endtime = time.time()
        print('처리시 간= ',endtime-starttime)
        # Break the loop if 'q' is pressed
        k_ = cv2.waitKey(1) & 0xFF
        if k_ == ord("q"):
            tcp.close()
            break
        elif k_ == ord('w'):  # w 누르면 프레임 멈추고 글자 읽기. 글자 읽기 성공 시 트래킹 시작
            if realsense:
                book_detector.get_image(RS)
            else :
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)
            ret, label_id, book_id = book_detector.ocr(word=find_word)
            if ret:
                tracking = True
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif k_ == ord('e'):
            if realsense:
                book_detector.get_image(RS)
            else :
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)
            book_detector.center_book(visualize=False)
            cv2.waitKey(0)

