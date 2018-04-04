import numpy as np
import cv2


img = cv2.imread('./data/0.jpg')
"""
修改大小 获取一部分照片 3通道分离
"""
# img = cv2.resize(img, (299, 299)) # 修改图片的大小
# cv2.imshow('img', img)
# eye = img[200:220, 210:230] # 获取一部分的图片
# cv2.imshow('roi', eye)
# b, g, r = cv2.split(img) # 与img[:, :, 0]等价 split的成本非常大 一般采用numpy index的方式

"""
给照片padding copyMakeBorder
"""
# BLUE = [255, 255, 255]
# replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
# cv2.imshow("constant", constant) # 加边框

"""
叠加两张图片
"""
# img1 = cv2.imread('./data/test_image.jpg')
# img1 = cv2.resize(img1, (299, 299))
# res = cv2.add(img, img1) # 1:1叠加
# res = cv2.addWeighted(img, 0.8, img1, 0.2, 0) # 按照权重进行叠加
# cv2.imshow("res", res)

"""
照片进行元素级别的操作 将img2放在img1的左上角
"""

# img1 = cv2.imread('./data/0.jpg')
# img2 = cv2.imread('./data/test_image.jpg')
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols ] # ROI是依据img2的大小而获取的img1相应地方的区域
#
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # 转黑白
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # 加阈值 黑白图片
# mask_inv = cv2.bitwise_not(mask) # 像素翻转  反黑白图片
# # 相当于在原图中抠出img2的样子  因为黑色是0 ,所以只要最后叠加就可以了
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv) # dst(I) = src1(I) & src2(I) if mask(I) != 0
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
#
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst
# cv2.imshow('res',img1)

"""
转换颜色空间并跟踪某个颜色物体
HSV空间比RBG空间更容易区分颜色
"""
# cap = cv2.VideoCapture(0)
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
# while(True):
#     if cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#             hsv_inrange = cv2.inRange(hsv_img, lower_blue, upper_blue) # 给图片加阈值 选取色彩某个区间内图片
#             res = cv2.bitwise_and(frame, frame, mask=hsv_inrange) # 根据不同的mask 自已与自己与可以只显示一部分要求的区域
#             cv2.imshow('res', res)
#             k = cv2.waitKey(5) & 0xFF
#             if k == 27:
#                 break
"""
缩放 变换 仿射变换等
"""

res = cv2.resize(img,(299, 299), interpolation = cv2.INTER_CUBIC)
cv2.imshow("res", res)
cv2.waitKey(-1)
cv2.destroyAllWindows()