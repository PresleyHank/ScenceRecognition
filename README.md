# ScenceRecognition
### CTPN+CRNN
This project is besed on [text-detection-ctpn](https://github.com/qq919056489/text-detection-ctpn) and [sceneReco](https://github.com/bear63/sceneReco).Because I don't have a Nvidia gpu,so this project is run on cpu mode.
## environment
- [x]  ubuntu16.04

- [x]  anaconda3

- [x] opencv3

- [x] tensorflow

- [x] pytorch

- [x] warp_ctc_pytorch

## about paper
CTPN:[Detecting Text in Natural Image with
Connectionist Text Proposal Network](https://arxiv.org/pdf/1609.03605.pdf)

CRNN:[An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition](https://arxiv.org/pdf/1507.05717.pdf)

## How to use
There has three directories and a file at the root directory of this project:

type | name | description
---|---|---
directory|ctpn|the module of ctpn
directory|crnn|the module of crnn
directory|imgs|the images that will be processed
file|demo.py|the main function of this project

# First

Download the model for crnn from baidu yun:[here](https://pan.baidu.com/s/1nvBV5FV).Then put it into **crnn/models**

# Second

Run install-cpu.sh , if there have some problem when run it , please open the file and execute single sentense.

There are two methods to run this project.

- If you have many images to be recognized,you can put them into **imgs/** and run **python demo.py**

- If you only have one or two images to be recognized,you can just run **python demo.py image1 image2 ...**


<img width="800" height="800" src="https://github.com/timekillmo/ScenceRecognition/blob/master/1.png" />
<img width="800" height="800" src="https://github.com/timekillmo/ScenceRecognition/blob/master/2.png" />

