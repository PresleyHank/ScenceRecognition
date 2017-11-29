from ctpn.ctpn.demo import get_text_box
from crnn.demo import *
import sys,os
sys.path.append(os.getcwd())

class CTPN_CRNN(object):

    # 文本检测
    def text_detection(self,im):
        img, text_recs = get_text_box(im)
        return img, text_recs

    # 文本识别
    def text_recognition(self,img, text_recs):
        model, converter = crnnSource()
        raw_preds, sim_preds = crnnRec(model=model, converter=converter, im=img, text_recs=text_recs)
        return raw_preds, sim_preds

    def do(self,img_name):
        # 读取图片
        im = cv2.imread(img_name)
        # 利用CTPN检测文本块
        img, text_recs = self.text_detection(im)
        # 使用CRNN识别文本
        raw_preds, sim_preds = self.text_recognition(img, text_recs)
        print("----------------------------------")
        # 输出识别结果
        for i in range(len(raw_preds)):
            print("%s" % (sim_preds[i]))


if __name__ == '__main__':
    ctpn_crnn = CTPN_CRNN()
    if len(sys.argv)==1:
        ctpn_crnn.do("imgs/1.png")
    else:
        for arg in sys.argv[1:]:
            ctpn_crnn.do(arg)
