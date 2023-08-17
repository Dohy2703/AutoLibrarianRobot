'''
test_easyocr_accuracy
'''

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import EasyOCR.easyocr.easyocr as easyocr
# import easyocr
from config import *
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import json

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

def calibrated_word(word):
    if 'z' in word:
        while 'z' in word:
            word = word.replace('z', '2')
    if '?' in word:
        while '?' in word:
            word = word.replace('?', '2')
    if '}' in word:
        while '}' in word:
            word = word.replace('}', '3')
    if ']' in word:
        while ']' in word:
            word = word.replace(']', '3')
    if 'J' in word:
        while 'J' in word:
            word = word.replace('J', '3')
    if 'j' in word:
        while 'j' in word:
            word = word.replace('j', '3')
    if 's' in word:
        while 's' in word:
            word = word.replace('s', '5')
    if 'e' in word:
        while 'e' in word:
            word = word.replace('e', '6')
    if 'a' in word:
        while 'a' in word:
            word = word.replace('a', '6')
    if 'C' in word:
        while 'C' in word:
            word = word.replace('C', '6')
    if 'g' in word:
        while 'g' in word:
            word = word.replace('g', '9')

    return word

def sharpening(image, strength):
    '''
    이미지 선명화
    :param image: 인풋 이미지
    :param strength: 선명화 정도
    :return: 아웃풋 이미지
    '''

    b = (1 - strength) / 8
    sharpening_kernel = np.array([[b, b, b],
                                  [b, strength, b],
                                  [b, b, b]])
    output = cv2.filter2D(image, -1, sharpening_kernel)
    return output


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
    # All_list = list_20_1
    # print(All_list)

    total_object = 0
    average_accuracy = 0
    average_calb_accuracy = 0

    temp_accuracy_list = []
    average_accuracy_list = []
    temp_calb_accuracy_list = []
    average_calb_accuracy_list = []
    result_dict = {
        "20_1":{'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{},
                 'p11':{}, 'p12':{}, 'p13':{}, 'p14':{}, 'p15':{}, 'p16':{}, 'p17':{}, 'p18':{}, 'p19':{}, 'p20':{}},
        "20_2": {'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{},
                 'p11':{}, 'p12':{}, 'p13':{}, 'p14':{}, 'p15':{}, 'p16':{}, 'p17':{}, 'p18':{}, 'p19':{}, 'p20':{}},
        "25_1": {'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{},
                 'p11':{}, 'p12':{}, 'p13':{}, 'p14':{}, 'p15':{}, 'p16':{}, 'p17':{}, 'p18':{}, 'p19':{}, 'p20':{}},
        "25_2": {'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{},
                 'p11':{}, 'p12':{}, 'p13':{}, 'p14':{}, 'p15':{}, 'p16':{}, 'p17':{}, 'p18':{}, 'p19':{}, 'p20':{}},
        "20_7": {'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{}},
        "25_8": {'p1':{}, 'p2':{}, 'p3':{}, 'p4':{}, 'p5':{}, 'p6':{}, 'p7':{}, 'p8':{}, 'p9':{}, 'p10':{}}
    }

    for idx, item in enumerate(All_list):
        start_time = time.time()

        print(item)
        img = cv2.imread(item)
        img = cv2.resize(img, (640, 480))

        # sharpening_img = sharpening(img, strength=3) # accuracy => 0.62
        sharpening_img = sharpening(img, strength=2)  # 0.6418
        # sharpening_img = sharpening(img, strength=1)  # 0.602

        # reader = easyocr.Reader(['ko', 'en'])
        reader = easyocr.Reader(['en'])  # 한글도 적용하고 싶으면 ['ko', 'en']. 다만 여기선 자음만 인식 안돼서 안씀
        # result = reader.readtext(img, slope_ths=0.3)
        result = reader.readtext(sharpening_img, slope_ths=0.3, allowlist="0123456789")

        exist_cnt = 0
        exist_list = []
        for word in books_model2[first_idx(idx)][second_idx(idx)].values():
            print('exist : ', word)
            exist_list.append(word)
            exist_cnt += 1
        result_dict[first_idx(idx)][second_idx(idx)]['exist'] = exist_list

        found_cnt = 0
        calb_found_cnt = 0
        found_list = []
        calibrated_found_list = []
        not_found_list = []
        for i in range(len(result)):
            for word in books_model2[first_idx(idx)][second_idx(idx)].values():
                if word in result[i][1]:
                    print('find : ', word)
                    found_list.append(word)
                    calibrated_found_list.append(word)
                    found_cnt+=1
                    calb_found_cnt += 1
                elif word in calibrated_word(result[i][1]):
                    calibrated_found_list.append(calibrated_word(word))
                    calb_found_cnt += 1
                elif len(result[i][1]) >= 6 and (result[i][1] not in not_found_list) and ('E' in result[i][1] or 'M' in result[i][1] or 'm' in result[i][1]):
                    not_found_list.append(result[i][1])

        delete_list = []
        for not_found_idx, not_found_item in enumerate(not_found_list):
            for found_item in found_list:
                if found_item in not_found_item:
                    delete_list.append(not_found_idx)

        delete_list.sort(reverse=True)
        for del_item in delete_list:
            try:
                not_found_list.pop(del_item)
            except:
                print('not found list : ', not_found_list)

        result_dict[first_idx(idx)][second_idx(idx)]['found'] = found_list
        result_dict[first_idx(idx)][second_idx(idx)]['calibrated_found'] = calibrated_found_list
        result_dict[first_idx(idx)][second_idx(idx)]['not_found_list'] = not_found_list

        temp_accuracy = found_cnt/exist_cnt
        temp_calb_accuracy = calb_found_cnt/exist_cnt

        average_accuracy += temp_accuracy*exist_cnt
        average_calb_accuracy += temp_calb_accuracy*exist_cnt
        total_object += exist_cnt

        temp_accuracy_list.append(temp_accuracy)
        temp_calb_accuracy_list.append(temp_calb_accuracy)

        average_accuracy_list.append(average_accuracy / total_object)
        average_calb_accuracy_list.append(average_calb_accuracy / total_object)

        dt = round(time.time() - start_time, 3)
        result_dict[first_idx(idx)][second_idx(idx)]['dt'] = dt

        print('dt : ', dt)
        print('accuracy : ', temp_accuracy, ', average_accuracy : ', average_accuracy / total_object)
        print(idx+1, '/', len(All_list))

        # 각 프레임에 걸린 시간초 추가
        # 글자 변환 규칙에 의한 정확도 추가

        # cv2.imshow('img', img)
        # cv2.waitKey(0)

    result_dict[first_idx(idx)]['average_accuracy'] = (average_accuracy / total_object)
    result_dict[first_idx(idx)]['average_calb_accuracy'] = (average_calb_accuracy / total_object)

    write_json = json.dumps(result_dict, indent=4, ensure_ascii=False)
    with open('/home/kdh/Desktop/example.json', 'w') as j:
        j.write(write_json)

    x = np.arange(0, len(All_list))
    avg_y = average_accuracy_list
    tmp_y = temp_accuracy_list
    plt.plot(x, tmp_y, color='#e35f62', marker='*', linewidth=2, label='tmp_accuracy')
    plt.plot(x, avg_y, color='forestgreen', marker='^', markersize=9, label='avg_accuracy')
    plt.plot(x,temp_calb_accuracy_list , color='red', marker='*', markersize=9, label='tmp_calb_accuracy')
    plt.plot(x, average_calb_accuracy_list, color='blue', marker='^', markersize=9, label='avg_calb_accuracy')
    plt.xlabel('X-axis')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

