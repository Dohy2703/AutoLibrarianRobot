from model import FAST
import torch 
from model.utils import fuse_module, rep_model_convert
from prepare_input import process_image
import cv2
import numpy as np
import time
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config.fast.tt import fast_base_tt_512_finetune_ic17mlt

def setup_fast():
    cfg = fast_base_tt_512_finetune_ic17mlt

    model = FAST()
    model = model.cuda()
    checkpoint = torch.load('model/weights.pth')
    state_dict = checkpoint['ema']
    d = dict()
    for key, value in state_dict.items():
        tmp = key.replace("module.", "")
        d[tmp] = value

    model.load_state_dict(d)
    model = rep_model_convert(model)
    model = fuse_module(model)
    model.eval()

    return model, cfg

def crop_imgs(image_path, model, cfg, visualize=False, count_time=True):
    if count_time:
        start_t = time.time()

    # image_path = './sample.png'
    img = cv2.imread(image_path)
    image = process_image(image_path)

    image['imgs']= image['imgs'].unsqueeze(0).cuda(non_blocking=True)

    with torch.no_grad():
        outputs = model(**image, cfg=cfg)
        result = outputs['results'][0]['bboxes']

    crop_img = []

    for bbox in result:
        points = np.array(bbox).reshape(-1,2)

        ''' visualize points '''
        # if visualize:
        #     for pt in points:
        #         cv2.circle(img, pt, 1, (0, 255, 0), 2)
        ''' visualize minarearect '''
        # if visualize:
        #     rect = cv2.minAreaRect(points)
        #     box = cv2.boxPoints(rect)
        #     box = np.intp(box)
        #     cv2.drawContours(img, [box], 0, (0,255,0), 3)
        ''' visualize bbox '''
        x, y, w, h = cv2.boundingRect(points)
        if visualize:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

        crop_img.append(img[y:y + h, x:x + w])
        if visualize:
            cv2.imshow('crop_img', img[y:y + h, x:x + w])
            cv2.waitKey(0)

    if count_time:
        end_t = time.time()
        print('reference time : ', end_t - start_t)

    if visualize:
        cv2.imshow('img', img)
        cv2.waitKey(0)

    return crop_img


def read_text_easyocr(crop_img):
    try:
        import EasyOCR.easyocr.easyocr as easyocr
    except:
        import easyocr  # pip install easyocr

    reader = easyocr.Reader(['en'])

    for item in crop_img:
        result = reader.recognize(item)
        for i in range(len(result)):
            print(result[i][1])

    # reader = easyocr.Reader(['en'])  # 한글도 적용하고 싶으면 ['ko', 'en']. 다만 여기선 자음만 인식 안돼서 안씀
    # result = reader.readtext(sharpening_img, slope_ths=0.3)


if __name__ == '__main__':
    model, cfg = setup_fast()
    fast_img = crop_imgs(image_path='./sample.png', model=model, cfg=cfg, visualize=False)
    # read_text_easyocr(fast_img)
