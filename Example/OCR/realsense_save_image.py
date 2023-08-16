import socket
import cv2
import pyrealsense2 as rs
import numpy as np

class realsense:
    def __init__(self):
        self.pipeline = rs.pipeline()       # 뎁스캠에서 프레임을 받아오는 걸 래핑
        self.config = rs.config()           # 프레임 configuration(창 크기, 해상도, frame rate)
        self.align = np.array([])           # RGB Cam과 stereo의 alignment(프레임, 초점 맞춰줌). 현재 RGB 시점
        self.color_image = np.array([])     # RGB 프레임 데이터(영상 데이터) - 데이터 형식이 0~2^8 (8bit).
                                            # image 붙은거 - opencv에서 rendering(호환)되게 끔 만든 데이터
        self.depth_image = np.array([])     # Depth 프레임 데이터(opencv에서 호환되도록 변환해준 행렬)
        self.distance_frame = np.array([])  # Depth 프레임의 raw 데이터 - 생으로 거리 행렬
        self.calib_data_path = 0            # *지금 안씀. 나중에 캘리브레이션 파라미터 받아오는 형식으로 사용할 것
        self.cam_mat = 0                    # *위와 동일
        self.dist_coef = 0                  # *위와 동일(캘리브레이션)
        self.r_vectors = 0                  # *위와 동일
        self.t_vectors = 0                  # *위와 동일(자세 추정) - 여기서 안씀
        self.depth_scale = 0                # 뎁스 스케일(metric -> mm).

    def set_cam(self,width,height,frame_rate):  # 파이프라인 설정
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = self.config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))
        found_rgb = False
        for s in device.sensors:
            # s => pipeline의 device정보 객체임.
            if s.get_info(rs.camera_info.name) == 'RGB Camera':
                found_rgb = True
                break
        if not found_rgb:
            print("The demo requires Depth camera with Color sensor")
            exit(0)
        self.config.enable_stream(rs.stream.depth, width, height, rs.format.z16, frame_rate)
        if device_product_line == "L500": # 이게 뭔지
            # config.enable_stream(rs.stream.color, 960,540,rs.format.bgr8,30)
            self.config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
        else:
            self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
            # config.enable_stream(rs.stream.color, 1280, 800, rs.format.bgr8, 30)
        profile = self.pipeline.start(self.config)
        depth_sensor = profile.get_device().first_depth_sensor()
        self.depth_scale = depth_sensor.get_depth_scale()
        print("Depth Scale is = ", self.depth_scale)
        align_to = rs.stream.color
        self.align = rs.align(align_to)

    def streaming(self):#, button):  # Yolov5 Dataloader의 update에 사용
        # while button:
        frames = self.pipeline.wait_for_frames()                # depth와 color map 둘다 가짐

        aligned_frames = self.align.process(frames)             # (color, depth)2가지 프레임 데이터를 캘브해주는 객체
        aligned_depth_frame = aligned_frames.get_depth_frame()  # (depth) color frame 기준으로 depth frame을 캘브한 객체
        color_frame = aligned_frames.get_color_frame()          # (color) align frame을 받아와서 color frame을 추출.
        color_image = np.asanyarray(color_frame.get_data())     # (color) 컬러 데이터를 opencv 호환 데이터로 변환
        depth_color_frame = rs.colorizer().colorize(aligned_depth_frame)    # (depth) rs 라이브러리에서 depth맵을 거리에 따라 컬러화
        depth_image = np.asanyarray(depth_color_frame.get_data())           # (depth) 컬러 데이터를 opencv 호환 데이터로 변환
        self.depth_image = depth_image
        self.color_image = color_image
        self.distance_frame = aligned_depth_frame

    def distance(self,x,y):         # depth의 raw값
        distance = self.distance_frame(x,y)
        print(distance)

    def show_image(self):           # 렌더링
        cv2.imshow("frame", self.color_image)
        cv2.imshow('depth', self.depth_image)


RS = realsense()
RS.set_cam(640,480,30)

import easyocr

idx = 1  # start idx
while True:
    RS.streaming()
    RS.show_image()
    key = cv2.waitKey(1)
    if key == ord("s"):
        cv2.imwrite('/home/kdh/Desktop/realsense_save/20_8/'+str(idx).zfill(2)+'.png', RS.color_image)
        idx += 1
    if key == ord("w"):
        reader = easyocr.Reader(['en'])  # 한글도 적용하고 싶으면 ['ko', 'en']. 다만 여기선 자음만 인식 안돼서 안씀
        result = reader.readtext(RS.color_image, slope_ths=0.3) # result = reader.readtext(self.label_masks, slope_ths=0.3)
        for i in range(len(result)):
            print(result[i][1])
        cv2.imshow('RS.color_image', RS.color_image)
        cv2.waitKey(0)

    if key == ord("q"):
        break
cv2.destroyAllWindows()
