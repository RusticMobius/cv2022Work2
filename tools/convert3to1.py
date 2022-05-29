##修改图片通道
import cv2
path = "/tools/ori"
import os
from PIL import Image
image_all = os.listdir(path)
for item in image_all:
    dir_all = os.path.join('', item)
    print(dir_all)
    name = dir_all.split("\\")[-1]

    img = cv2.imread(dir_all)  ##注意cv2.imread（）里边的路径是相对路径
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 转成PIL格式
    res_image = image.convert('P')  # 保存为P格式
    res_image.save("processed" + "/" + name)



