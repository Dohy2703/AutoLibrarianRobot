import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import EasyOCR.easyocr.easyocr as easyocr
import easyocr
from config import *
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

def first_idx(idx):
    if (idx < 20):
        return '20_1'
    elif (idx < 40):
        return '20_2'
    elif (idx < 60):
        return '25_1'
    elif (idx < 80):
        return '25_2'
    elif (idx < 90):
        return '20_7'
    elif (idx < 100):
        return '25_8'

def second_idx(idx):
    if (idx < 20):
        return 'p'+str(idx+1)
    elif (idx < 40):
        return 'p' + str(idx - 20 + 1)
    elif (idx < 60):
        return 'p' + str(idx - 40 + 1)
    elif (idx < 80):
        return 'p' + str(idx - 60 + 1)
    elif (idx < 90):
        return 'p' + str(idx - 80 + 1)
    elif (idx < 100):
        return 'p' + str(idx - 90 + 1)


if __name__ == '__main__':
    path = '/home/kdh/Desktop/realsense_save/'
    
    list_20_1 = glob.glob(path+'20_1/*.png')
    list_20_1.sort()
    list_20_2 = glob.glob(path+'20_2/*.png')
    list_20_2.sort()
    list_25_1 = glob.glob(path+'25_1/*.png')
    list_25_1.sort()
    list_25_2 = glob.glob(path+'25_2/*.png')
    list_25_2.sort()
    list_20_7 = glob.glob(path+'20_7/*.png')
    list_20_7.sort()
    list_25_8 = glob.glob(path+'25_8/*.png')
    list_25_8.sort()

    All_list = list_20_1 + list_20_2 + list_25_1 + list_25_2 + list_20_7 + list_25_8
    print(All_list)

    average_accuracy = 0
    temp_accuracy_list = []
    average_accuracy_list = []


    for idx, item in enumerate(All_list):
        print(item)
        img = cv2.imread(item)
        img = cv2.resize(img, (640, 480))
        reader = easyocr.Reader(['en'])  # 한글도 적용하고 싶으면 ['ko', 'en']. 다만 여기선 자음만 인식 안돼서 안씀
        result = reader.readtext(img, slope_ths=0.3)

        exist_cnt = 0
        for word in books_model2[first_idx(idx)][second_idx(idx)].values():
            print('exist : ', word)
            exist_cnt += 1

        find_cnt = 0
        for i in range(len(result)):
            for word in books_model2[first_idx(idx)][second_idx(idx)].values():
                if word in result[i][1]:
                    print('find : ', word)
                    find_cnt+=1

        temp_accuracy = find_cnt/exist_cnt
        average_accuracy += temp_accuracy
        temp_accuracy_list.append(temp_accuracy)
        average_accuracy_list.append(average_accuracy / (idx + 1))

        print('accuracy : ', temp_accuracy, ', average_accuracy : ', average_accuracy / (idx + 1))
        print(idx+1, '/', len(All_list))

        # 각 프레임에 걸린 시간초 추가
        # 글자 변환 규칙에 의한 정확도 추가

        # cv2.imshow('img', img)
        # cv2.waitKey(0)

    x = np.arange(0, len(All_list))
    avg_y = average_accuracy_list
    tmp_y = temp_accuracy_list
    plt.plot(x, tmp_y, color='#e35f62', marker='*', linewidth=2, label='tmp_accuracy')
    plt.plot(x, avg_y, color='forestgreen', marker='^', markersize=9, label='avg_accuracy')
    plt.xlabel('X-axis')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

