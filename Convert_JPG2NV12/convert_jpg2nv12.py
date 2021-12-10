import os
import cv2
from ffmpy3 import FFmpeg

in_path = "./jpgs/"
out_path = "./yuvs/"
dirs = os.listdir(in_path)

for in_file in dirs:
    ## read image
    img = cv2.imread(in_path + in_file)

    ## convert & save image
    out_file = in_file.split("/")[-1].split(".")[0] + ".yuv"
    size = '{}x{}'.format(img.shape[1],img.shape[0]) 
    ff = FFmpeg(inputs={in_path+in_file:None},
                    outputs={out_path+out_file:'-s {} -pix_fmt nv12'.format(size)})
    print(ff.cmd)
    ff.run()
    del img

