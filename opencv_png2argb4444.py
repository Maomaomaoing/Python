
import os
from PIL import Image
import cv2
import numpy as np

def BGRA8888_to_ARGB4444(img):
    # shape: (height, width, 4)
    # input format: BGRA8888 (4 channels, 8 bits each)
    # output format: ARGB4444 (4 channels, 4 bits each)
    img = img.astype(np.uint16)  # Ensure the image is in uint16 format, cus we'll concatenate channels into 16 bits later
    b4 = (img[:,:,0] >> 4) & 0xF
    g4 = (img[:,:,1] >> 4) & 0xF
    r4 = (img[:,:,2] >> 4) & 0xF
    a4 = (img[:,:,3] >> 4) & 0xF
    
    argb4444 = (a4 << 12) | (r4 << 8) | (g4 << 4) | b4

    return argb4444 

#转化后的文件夹名称
 
# 读取图像
filename = "box.png"

img8888 = cv2.imread(filename, -1) # BGRA8888格式
print(img8888.shape)

# save only B channel
cv2.imwrite("B.png", img8888[:, :, 0])
cv2.imwrite("G.png", img8888[:, :, 1])
cv2.imwrite("R.png", img8888[:, :, 2])
cv2.imwrite("A.png", img8888[:, :, 3])

#轉換成ARGB4444格式
img4444 = BGRA8888_to_ARGB4444(img8888)
print(img8888.shape, img4444.shape)

# 保存图像至二進位文件
with open("box_8888.bin", 'wb') as f:
    f.write(img8888.tobytes())

with open("box_4444.bin", 'wb') as f:
    f.write(img4444.tobytes())
