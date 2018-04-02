import numpy as np
import cv2 as cv

# img = cv.imread('./data/test_image.jpg') # 读入图片
# cv.imshow('image', img) # 展示图片
# cv.imwrite('./data/save_image.jpg', img)
"""
图片的信息读入
"""
# img = cv.imread('./data/test_image.jpg') # 读入图片
# cv.imshow('image', img) # 展示图片
# cv.imwrite('./data/save_image.jpg', img)

"""
视频信息操作---从摄像头获取视频 或者是本地获取  然后进行保存
"""
# cap = cv.VideoCapture(0) # 可以是0表示摄像头 也可以是本地的视频路径
# fourcc = cv.VideoWriter_fourcc(*'MPEG')
# out_video = cv.VideoWriter('./data/camera.avi', fourcc, 30, (1280, 720)) # opencv 只支持AVI格式的
# while(cap.isOpened()):
#     ret, frame = cap.read() # ret是检查读入的状态的
#     if ret:
#         # gray = cv.cvtColor(frame, cv.C OLOR_BGR2GRAY)
#         # cv.imwrite('./data/' + str(i) + '.jpg', frame) # 保存为帧
#         frame = cv.flip(frame, -1) # 图片进行翻转 0-x上下翻转 1-y水平翻转 -1-xy轴
#         out_video.write(frame) # 之前不能有同名的视频,否则会报错
#     else:
#         break
# cap.release()
# out_video.release()

"""
有关绘图的函数
"""
# img = np.zeros((299, 299, 3), np.uint8)  # uint8 无符号整数
# cv.line(img, (0, 0), (288, 288), (255, 255, 255), 1)
# cv.rectangle(img, (2, 0), (88, 88), (0, 255, 0), 3)
# cv.imwrite("./line.jpg", img)


"""
鼠标作为画笔
"""
# drawing = False # true if mouse is pressed
# ix,iy = -1,-1 # 全局变量要写在外面, 因为是不断的回调draw_circle函数
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix, iy, drawing
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             cv.line(img, (ix, iy), (x, y), (255, 255, 255), 1)
#             ix, iy = x, y
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#
#
#
# # 创建图像窗口并将窗口与回调函数绑定
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF # cv.waitKey(0) 用于暂停显示图片 cv.waitKey(1)返回一个32bit的整数,但是ascii值是8位的, 按位与只用拿到后面的8位可以
#     if k == 27: # 27 是ASCII值,esc是27
#         break
# cv.destroyAllWindows()

"""
进度条 调整RGB3色
"""

def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image-RGB')
cv.createTrackbar('R','image-RGB',0,255,nothing)
cv.createTrackbar('G','image-RGB',0,255,nothing)
cv.createTrackbar('B','image-RGB',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image-RGB',0,1,nothing)
while(1):
    cv.imshow('image-RGB',img)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image-RGB')
    g = cv.getTrackbarPos('G','image-RGB')
    b = cv.getTrackbarPos('B','image-RGB')
    s = cv.getTrackbarPos(switch,'image-RGB')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()

