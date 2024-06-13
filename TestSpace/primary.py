import cv2
import numpy
import matplotlib.pyplot as plt
import numpy as np

# 读取彩色图像/参数(str..)
# OpenCV提供BGR,matplotlib需求RGB,使用cvtColor进行转换
img1 = cv2.imread("tg.jpg")
img_1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread('mt.jpg')
img_2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3 = cv2.imread("ey.png")

titles = ['tg','mt']
images = [img_1,img_2]
#
# # 显示图像/等待显示
# cv2.imshow("Demo_pic",img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 使用matplotlib显示所有图像
# for i in range(2):
#     plt.subplot(2,1,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
#
# # 将一片区域设置为指定的像素
# # img.shape返回元组(y,x,通道数)
# # 通道数通常为3,或许会有一个透明通道alpha,可为4
# print(img2.shape)
# height, width = img1.shape[:2]
# # 将指定区域的像素更改为指定数据
# img1[100:200,150:250] = [255,255,255]
#
# # 使用numpy读取/修改指定(y,x,通道)的像素
# print(img1.item(78,100,0))
# img1.itemset((78,100,0),100)

# openCV创建空图像-Numpy-zeros(np.uint8为指定格式)/zeros_like
emptyImage1 = np.zeros(img1.shape,np.uint8)
emptyImage2 = np.zeros_like(img1)

# 输出图像到指定文件imwrite(filename,img,[params])
# *params 表示特定格式保存的参数编码，默认值为空。对于 JPEG 图
# *片，该参数（ cv2.IMWRITE_JPEG_QUALITY ）表示图像的质量
# *用 0 100 的整数表示，默认值为 95 。对于 PNG 图片，该参数
# *cv2.IMWRITE_PNG_COMPRESSION ）表示的是压缩级别
# *从 0 到 9 ，压缩级别越高，图像尺寸越小，默认级别为 3 。对于 PPM 、
# *PGM 、 PB M 图片，该参数表示一个二进制格式的标志
# *cv2.IMWRITE_PXM_BINARY ））[ 。注意，该类型为 Long ，必
# *须转换成 int 。
# ---------------------------------
# 保存图像img1,并使用JPEG压缩格式,程度为90
cv2.imwrite("output.jpg",img1,[cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite('output.png',img3,[cv2.IMWRITE_PNG_COMPRESSION, 3])



