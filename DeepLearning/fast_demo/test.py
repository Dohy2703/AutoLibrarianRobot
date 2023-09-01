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

cfg = fast_base_tt_512_finetune_ic17mlt

if __name__ == '__main__':
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

    start_t = time.time()

    image_path = './sample.png'
    img = cv2.imread(image_path)
    image = process_image(image_path)

    image['imgs']= image['imgs'].unsqueeze(0).cuda(non_blocking=True)

    with torch.no_grad():
        outputs = model(**image, cfg=cfg)
        result = outputs['results'][0]['bboxes']

    for bbox in result:
        points = np.array(bbox).reshape(-1,2)
        # for pt in points:
        #     cv2.circle(img, pt, 1, (0, 255, 0), 2)
        rect = cv2.minAreaRect(points)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        cv2.drawContours(img, [box], 0, (0,255,0), 3)

    end_t = time.time()
    print('reference time : ', end_t - start_t)

    cv2.imshow('img', img)
    cv2.waitKey(0)
