from collections import defaultdict
import cv2
from ultralytics import YOLO
from realsense import Realsense
from detect_book import DetectBook

#(창민) 캘리브레이션 데이터 경로
calb_path = '/home/chad-chang/PycharmProjects/23_HF071/calib_data/MultiMatrix.npz'
realsense = True  # 지역변수 오류때문에 미리 선언해둠

if __name__ == '__main__':
    """ 이 두 개만 True / False 바꾸도록 하자 """
    kdh = True  # 도현
    ChadChang = False  # 창민

    # Instances
    if kdh:
        model = YOLO('/home/kdh/Downloads/best_v8.pt')
        book_detector = DetectBook(0)
        realsense = False  # True면 뎁스카메라, False면 비디오
    elif ChadChang:
        model = YOLO('/home/chad-chang/PycharmProjects/23_HF071/best.pt')
        book_detector = DetectBook(calb_path)
        realsense = True  # True면 뎁스카메라, False면 비디오

    # Flags
    tracking = False  # 글자 읽었을 때 트래킹
    detect_center_book = False   #  중앙에 있는 책을 계속 검출할 것인지.
    if realsense:
        RS = Realsense()
    else:  # video
        cap = cv2.VideoCapture('/home/kdh/Downloads/20230801_002342.mp4')

    # Lists
    track_history = defaultdict(lambda: [])

    # Local variable 문제 해결
    frame = []
    book_id = 0
    label_id = 0

    # Loop through the video frames
    while True:
        if realsense:
            results = model.track(RS.color_image, persist=True) # Run YOLOv8 tracking on the frame, persisting tracks between frames
            book_detector.get_image(RS)
        else :  # video
            _, frame = cap.read()
            frame = cv2.resize(frame, (640, 384))
            results = model.track(frame, persist=True)

            book_detector.get_video_image(frame)

        if detect_center_book and len(results[0].boxes):  # 중앙의 책을 검출하는 플래그
            ret = book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)
            if ret==0:
                book_detector.center_book()

        if results[0].boxes!=None and results[0].boxes.id!=None:
            annotated_frame = results[0].plot() # Visualize the results on the frame
            if tracking:  # w 누르고 글자를 읽기 성공 시 트래킹
                book_idx = results[0].boxes.id.int().cpu().tolist().index(book_id)
                label_idx = results[0].boxes.id.int().cpu().tolist().index(label_id)
                cv2.imshow('trackB', results[0].masks.data[book_idx].cpu().numpy())
                cv2.imshow('trackL', results[0].masks.data[label_idx].cpu().numpy())

            cv2.imshow("YOLOv8 Tracking", annotated_frame)
        else:  # not tracking
            cv2.imshow("YOLOv8 Tracking", results[0].plot())

        # 키보드 입력 이벤트 -> 나중에 ROS 통신으로 변경할 것
        k_ = cv2.waitKey(1) & 0xFF
        if k_ == ord("q"):
            break

        elif k_ == ord('w'):  # w 누르면 프레임 멈추고 글자 읽기. 글자 읽기 성공 시 트래킹 시작
            if realsense:
                book_detector.get_image(RS)
            else :
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)
            ret, label_id, book_id = book_detector.ocr(word=623400)
            if ret:
                tracking = True
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif k_ == ord('e'):  # e 누르면 중앙 책 검출
            if realsense:
                book_detector.get_image(RS)
            else :
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names)
            book_detector.center_book()
            cv2.waitKey(0)
