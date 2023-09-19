from cam_operator import Operator
from ultralytics import YOLO
from realsense import Realsense
from detect_book import DetectBook
from TCPmanager import TCP
from label_reader import labelReader

from collections import defaultdict
from collections import deque  # status queue로 정의하기
import time
import cv2
import numpy as np
import math as m
import argparse


# status = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def librarian_main(
        yolov8_weights=None,  # model.py path
        source='/home/kdh/Downloads/20230801_002342.mp4',
        realsense=True,  # realsense
        status='0',
        find_word=62290,
        book_detector = None,
        ip = '127.0.1.1',
        port = 2014,
        tcp_available = False,
        query = None,
):
    img_fm = cv2.imread('/home/kdh/Desktop/material.png')
    FeatureMatcher = cv2.AKAZE_create()

    kdh = True
    ChadChang = False
    '''state마다 동작을 정해주는 클래스를 따로 만들음'''

    if kdh:
        model = YOLO('/home/kdh/Downloads/best_v8.pt')
        book_detector = DetectBook(0)
        realsense = False  # True면 뎁스카메라, False면 비디오
    elif ChadChang:
        runner = Operator()
        # calb_path = '/home/chad-chang/PycharmProjects/23_HF071/calib_data/MultiMatrix.npz'
        calb_path = './MultiMatrix.npz'
        # model = YOLO('/home/chad-chang/PycharmProjects/23_HF071/best.pt')
        model = YOLO('/home/kdh/Downloads/best_v8.pt')
        book_detector = DetectBook(calb_path)
        realsense = True  # True면 뎁스카메라, False면 비디오q
        tcp = TCP(ip, port, available=tcp_available)

    # if yolov8_weights != None:
    #     model = YOLO(yolov8_weights)

    # Flags
    tracking = False  # 글자 읽었을 때 트래킹
    detect_center_book = True  # 말 그대로 중앙에 있는 책을 계속 검출할 것인지.

    if realsense:
        RS = Realsense()
    else:  # video
        cap = cv2.VideoCapture(source)

    # reader instance
    book_detector.setup_reader()

    # Lists
    track_history = defaultdict(lambda: [])

    frame = []
    book_id = 0
    label_id = 0

    # Loop through the video frames
    while True:
        starttime = time.time()
        if realsense:
            results = model.track(RS.color_image,
                                  persist=True)  # Run YOLOv8 tracking on the frame, persisting tracks between frames
            book_detector.get_image(RS)
        else:  # video
            _, frame = cap.read()
            frame = cv2.resize(frame, (640, 384))
            results = model.track(frame, persist=True)
            book_detector.get_video_image(frame)

        if ChadChang:
            # 유석 (아두이노-> 매트랩 -> 파이썬)
            '''status0 : 통신 대기'''
            # print(runner.run_readable(book_detector,results, visual=True))

            if status == '0':
                # tcp.
                print("status0 = ", status)
                status_buff = tcp.receive()  # 통신받은 값은 값은 status값임
                print("status _buff = ", status_buff)
                if status_buff:
                    print("buf = true")
                    status = status_buff
                    # print('status = 0->1', status)

                '''status1 : 책 읽으러 동작'''  # 조금 수정할 필요있을듯
            elif status == '1':  # 책 읽으러 동작
                print("status1 = ", status)
                if not wait:
                    # ret_r = detect_center_book.read_center_word(visualize = True)
                    ret_r, H = runner.run_approach(book_detector, results, visual=True)
                    print("H mat = ", H)
                    # print(ret_r)
                    # print(runner.TF)
                    # 보내는 값이 온전한지 확인
                    # 통신 보내는 것필요
                    if ret_r:  # 특징 추출 완료하면
                        tcp.send(H, matrix=True)
                        wait = True
                status_buff = tcp.receive()
                if status_buff:
                    print("buf = true")
                    status = status_buff
                    # print('status = 1->2', status)
                    wait = False

                    # 잠깐 쉬는 시간 가질까

                '''status2 : 글자 읽기 + 오차 계산'''
            elif status == '2':  # readable한지 판단 & 방향 통신
                print("status2 = ", status)
                if not wait:
                    ret, dir = runner.run_readable(book_detector, results, visual=True)
                    if (not ret and dir != None):  # 아무것도 안 잡힐때
                        print(dir)
                        tcp.send(dir)
                        wait = True
                    else:  # 읽을 수 있을때
                        tcp.send(2.5)
                        # tcp.send(3)
                        print("readable")
                        wait = True
                status_buff = tcp.receive()
                # print("status2 =", status_buff)
                if status_buff:
                    print("buf = true", status_buff)
                    status = status_buff
                    wait = False

            elif status == '9':  # 글씨 확인
                print("status9 = ", status)
                ret_r = runner.read_ocr(book_detector, results, find_word, visual=True)
                if ret_r:
                    status = '3'
                    print("status_trans = ", 3)
                    tcp.send(3)  # 글씨 읽지 못한경우
                else:  # 글씨 읽기 실패했을 때
                    status = '8'
                    print("status_trans = ", 8)
                    # tcp.send(8)

                # if ret_r_:
                #     ret_r_ = book_detector.read_center_word(visualize=False)
                #     query = book_detector.center_word
                #     query = int(query)
                #     print('reading = ', query)
                #     print(type(query))
                #     print(type(find_word))
                #     # print()
                #     print(query == find_word)
                # if find_word == query:
                #     print("same query")
                #     # ret_r = runner.read_ocr(book_detector, results, find_word, visual = True)
                #     # if ret_r: # 읽었을 때 status3으로 가라
                #     tcp.send(3)  # 글씨 읽지 못한경우
                #     print('status = 2->3', status)
                #     print('word is f{}',find_word)
                #     status = '3'

                # else: # 못 읽었으면 8번 상태로 가라 또는 다시 읽을까
                #     print('can not find the ')
                #     print('status = 2->8', status)
                #     tcp.send(8) # 글씨 읽지 못한경우
                #     status = '8'
                # print('status =', status)

                '''status3: 해당 책 위치로 이동'''
            elif status == '3':  # 해당책 위치로 이동:
                # cv2.imshow("depth", book_detector.depth_image)
                print("status3 = ", status)
                # ret_r, H = runner.read_estimate(book_detector, results, visual=True)
                if not wait:
                    ret_r, H = runner.read_estimate(book_detector, results, visual=True)
                    print(ret_r, H)
                    # 보내는 값이 온전한지 확인
                    # 통신 보내는 것 필요
                    if ret_r:  # 특징 추출 완료하면
                        wait = True
                        tcp.send(H, matrix=True)
                    else:  # 추출이 실패하면
                        wait = False

                status_buff = tcp.receive()
                if status_buff:
                    print("buf = true")
                    status = status_buff
                    wait = False
                    # print('status = 3->5', status)  #트래킹하는 부분은 보류됨
                    status = '5'
                    # 잠깐 쉬는 시간 가질까

            elif status == '4':  # 트래킹하면서 좌표 보내주기
                if results[0].boxes != None and results[0].boxes.id != None:
                    annotated_frame = results[0].plot()  # Visualize the results on the frame
                    if tracking:  # w 누르고 글자를 읽기 성공 시 트래킹
                        book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names,
                                               tracking=tracking)  # 마스크 검출
                        label_id, book_id, label_idx, book_idx = book_detector.IDcheck(label_id, book_id)
                        if label_id == -1 and book_id == -1:
                            tracking = False
                            print('tracking = False')
                        else:
                            book_detector.tracking_getter(label_idx, book_idx,
                                                          visualize=True)  # 글자 읽은 책, 글자 읽은 라벨지, 책+라벨지 트래킹
                            # 좌표 통신해 줌
                    cv2.imshow("YOLOv8 Tracking", annotated_frame)
                else:  # not tracking
                    cv2.imshow("YOLOv8 Tracking", results[0].plot())




            elif status == '5':  # 최종적으로 넣기전에 그리퍼 align 맞추
                print("status5 = ", status)
                if not wait:
                    lc_point, blc_point = book_detector.LC_point, book_detector.BLC_point
                    # print(lc_point,blc_point)
                    ang = book_detector.calc_ang(lc_point, blc_point, visual=True)
                    print("angle = ", ang)
                    if ang:
                        tcp.send(ang)
                wait = True
                status_buff = tcp.receive()
                if status_buff:
                    print("buf = true")
                    # if -1 < ang < 1:
                    status = status_buff
                    wait = False
                    # print('status = 5->6', status)

            elif status == '6':  # 넣고 있을때 통신 기다리는 모드
                print("status6 = ", status)
                status_buff = tcp.receive()
                if status_buff:
                    print("buf = true", status_buff)
                    status = status_buff  # fail of suceed

            # elif status == '7':  # 그리핑 성공 여부 판단
            #     status_buff = tcp.receive
            #     if status_buff:
            #         status = 10

            # elif status == :

            elif status == '8':  # 해당 프레임에 책이 없을때 + 목표 책을 못 읽었을 경우도 있음(책 인식 모델이 매우 정확도가 높은 것이기 때문에 고려하지 않기)
                tcp.send(1)  # not read symbol
                print("status8 = ", status)
                status_buff = tcp.receive()
                if status_buff:
                    print("buf = true")
                    status = status_buff
                # if not wait:
                #     print(runner.TF)
                #     # 보내는 값이 온전한지 확인
                #     # 통신 보내는 것필요
                #     if ret_r:  # 특징 추출 완료하면
                #         tcp.send(H, matrix=True)
                #     wait = True
                # status_buff = tcp.receive()
                # if status_buff:
                #     status = status_buff
                #     print('status = 1->2', status)
                #     wait = False


            elif status == 'f':  # 로봇팔 구동이 끝나고 유석이 쪽으로 신호줄때
                status_buff = tcp.receive()

            # elif status == 's':

        if results[0].boxes != None and results[0].boxes.id != None:
            annotated_frame = results[0].plot()  # Visualize the results on the frame
            if tracking:  # w 누르고 글자를 읽기 성공 시 트래킹
                book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names,
                                       tracking=tracking)  # 마스크 검출
                label_id, book_id, label_idx, book_idx = book_detector.IDcheck(label_id, book_id)
                if label_id == -1 and book_id == -1:
                    tracking = False
                    print('tracking = False')
                else:
                    book_detector.tracking_getter(label_idx, book_idx, visualize=True)  # 글자 읽은 책, 글자 읽은 라벨지, 책+라벨지 트래킹
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            ## feature matching
            img_fm2 = book_detector.color_image
            # feature matching 시도
            kp1, des1 = FeatureMatcher.detectAndCompute(img_fm, None)
            kp2, des2 = FeatureMatcher.detectAndCompute(img_fm2, None)

            # 매칭 알고리즘 선정
            FLANN_INDEX_LSH = 6
            index_params = dict(algorithm=FLANN_INDEX_LSH,
                                table_number=6,
                                key_size=12,
                                multi_probe_level=1)
            search_params = dict(checks=32)
            matcher = cv2.FlannBasedMatcher(index_params, search_params)

            # 매칭 및 매칭된 포인트 거리 정렬
            matches = matcher.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            good_matches = matches[:30]

            # 매칭 결과 시각화
            img3 = cv2.drawMatches(img_fm, kp1, img_fm2, kp2, good_matches, None, flags=2)
            cv2.imshow("Matching result", img3)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            # 매칭된 지점의 픽셀 위치 추출
            matched_points1 = []
            matched_points2 = []
            for match in good_matches:
                # queryIdx: 첫 번째 이미지에서의 키포인트 인덱스
                # trainIdx: 두 번째 이미지에서의 키포인트 인덱스
                pt1 = kp1[match.queryIdx].pt
                pt2 = kp2[match.trainIdx].pt
                matched_points1.append((int(pt1[0]), int(pt1[1])))
                matched_points2.append((int(pt2[0]), int(pt2[1])))

            # 픽셀 위치 출력
            print("Matched Points in Image1:", matched_points1)
            print("Matched Points in Image2:", matched_points2)


        else:  # not tracking
            cv2.imshow("YOLOv8 Tracking", results[0].plot())


        endtime = time.time()
        # print('처리시 간= ',endtime-starttime)
        # Break the loop if 'q' is pressed
        k_ = cv2.waitKey(1) & 0xFF
        if k_ == ord("q"):
            tcp.close()
            break

        elif k_ == ord('w'):  # w 누르면 프레임 멈추고 글자 읽기. 글자 읽기 성공 시 트래킹 시작
            if realsense:
                book_detector.get_image(RS)
            else:
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names, tracking=tracking)
            ret, label_id, book_id = book_detector.ocr(word=find_word)
            if ret:
                tracking = True
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif k_ == ord('e'):
            if realsense:
                book_detector.get_image(RS)
            else:
                book_detector.get_video_image(frame)
            book_detector.get_mask(results[0].boxes.cpu(), results[0].masks.data, results[0].names, tracking=tracking)
            book_detector.center_book(visualize=True)
            # book_detector.BLC_point
            # ret_r, H = runner.run_approach(book_detector, results, visual = True)
            cv2.waitKey(0)

        elif k_ == ord('f'):  # feature matching
            if realsense:
                book_detector.get_image(RS)
            else:
                book_detector.get_video_image(frame)






def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='./best_v8.pt', help='yolov8 model path(s)')
    parser.add_argument('--source', type=str, default=None, help='source other than realsense')
    parser.add_argument('--realsense', type=bool, default=True, help='if you use realsense depth cam')
    parser.add_argument('--status', type=str, default='0', help='initial robot arm status')
    parser.add_argument('--find-word', type=int, default=623400, help='book label number to find')
    parser.add_argument('--book-detector', default=None, help='detectBook instance')
    parser.add_argument('--ip', type=str, default='127.0.1.1', help='tcp ip communication')
    parser.add_argument('--port', type=int, default=2014, help='tcp ip port')
    parser.add_argument('--tcp-available',type=bool, default=True, help='tcp available')
    parser.add_argument('--query', default=None, help=' ')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    librarian_main(opt)