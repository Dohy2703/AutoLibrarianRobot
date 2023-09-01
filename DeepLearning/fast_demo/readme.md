
*Thanks to* <br/>
  https://github.com/czczup/FAST<br/>
  https://github.com/Chappie74/fast_demo<br/><br/>


*Change log*
fast_head.py <br/>
  line6 | from ..utils import generate_bbox --> from ..utils.generate_bbox import generate_bbox <br/>

prepare_input.py <br/>
  line47 | org_img_size=np.array(img.shape[:2]) --> org_img_size=[np.array(img.shape[:2])]<br/>
  line52 | img_size=np.array(img.shape[:2]), --> img_size=[np.array(img.shape[:2])],<br/>

generate_bbox.py <br/>
  line15 | if points.shape[0] < cfg.test_cfg.min_area : --> if points.shape[0] < cfg.test_cfg['min_area']: <br/>
  line19 | if score_i < cfg.test_cfg.min_score : --> if score_i < cfg.test_cfg['min_score']: <br/>
  line23 | if cfg.test_cfg.bbox_type == 'rect': --> if cfg.test_cfg['bbox_type'] == 'rect': <br/>
  line29 | elif cfg.test_cfg.bbox_type == 'poly': --> elif cfg.test_cfg['bbox_type'] == 'poly': <br/><br/>

  added (line5~8)<br/>
  import os<br/>
  import sys<br/>
  sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) <br/>
  from fast_demo.config.fast.tt import fast_base_tt_512_finetune_ic17mlt as cfg<br/>



