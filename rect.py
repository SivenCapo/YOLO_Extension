from pickle import TRUE
from telnetlib import DO
import cv2
import numpy as np
import random

def yolo_to_pixel_coords(yolo_coords, image_width, image_height):
    x_center, y_center, width, height = yolo_coords

    x_min = int((x_center - width / 2) * image_width)
    y_min = int((y_center - height / 2) * image_height)
    x_max = int((x_center + width / 2) * image_width)
    y_max = int((y_center + height / 2) * image_height)

    return x_min, y_min, x_max, y_max




# 假设这是一系列坐标点，以元组的形式表示
points = [(random.randint(50, 250), random.randint(50, 250)) for _ in range(20)]

# 将坐标点转换为NumPy数组
points_np = np.array(points)
print(points_np)
# 计算边与坐标轴平行的最小外接矩形
x, y, w, h = cv2.boundingRect(points_np)

# 创建一个空白图像
image = np.zeros((300, 300, 3), dtype=np.uint8)

# 绘制原始坐标点
for point in points:
      cv2.circle(image, point, 3, (0, 0, 255), -1)

# 绘制边与坐标轴平行的最小外接矩形
cv2.rectangle(image, (x-2, y-2), (x + w+2, y + h+2), (255, 255, 0), 2)

# 显示图像
cv2.imshow("Bounding Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()