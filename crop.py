import cv2
import os
import numpy as np
import random
import matplotlib.pyplot as plt


result_folder = "result5"
output_folder = "crop5"
labels_folder = "labels5"
image_files = [filename for filename in os.listdir(result_folder) if filename.endswith(".jpg")]


for image_file in image_files:
    # 读取图片
    image_path = os.path.join(result_folder, image_file)
    image = cv2.imread(image_path)
    #读取yolo数据
    label_file = os.path.join(labels_folder, image_file.replace(".jpg", ".txt"))
    with open(label_file, "r") as f:
      lines = f.readlines()

    #初始化数组
    points=[]

    for line in lines:
       class_id, x_center, y_center, width, height = map(float, line.strip().split())
       x_min = int((x_center - width / 2) * image.shape[1])
       y_min = int((y_center - height / 2) * image.shape[0])
       x_max = int((x_center + width / 2) * image.shape[1])
       y_max = int((y_center + height / 2) * image.shape[0])
       points.append((x_min,y_min))
       points.append((x_max,y_min))
       points.append((x_min,y_max))
       points.append((x_max,y_max))
       print(x_min,x_max,y_min,y_max)
    
    points_np = np.array(points)
    print(points_np)

# 计算边与坐标轴平行的最小外接矩形
    x, y, w, h = cv2.boundingRect(points_np+1)
    print(x,y,w,h)

# 绘制原始坐标点
#     for point in points:
#         cv2.circle(image, point, 3, (0, 0, 255), -1)

# # 绘制边与坐标轴平行的最小外接矩形
#     cv2.rectangle(image, (x-2, y-2), (x + w+2, y + h+2), (255, 255, 0), 2)

# # 显示图像
#     cv2.imshow("Bounding Rectangle", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


    #处理五次  
    for i in range(5): 
      y1, x1 = int(h/2), int(w/2)
      random_integer1 = random.randint(0,7)
      random_integer2 = random.randint(0,5)
      y_r , x_r = int(y1*random_integer1/2) , int(x1*random_integer2/4)

      y_start = y-y_r
      y_end = y+h+y_r
      x_start = x-x_r
      x_end = x+w+x_r
      print(y_start,y_end,x_start,x_end)
      cropped_image = image[y_start:y_end, x_start:x_end]
    #   cv2.imshow("Cropped Image", cropped_image)
    #   cv2.waitKey(0)  # 等待按下任意按键
    #   cv2.destroyAllWindows()  # 关闭窗口
      cropped_image_path = os.path.join(output_folder, f"cropped_{i+1}_{image_file}")
      cv2.imwrite(cropped_image_path, cropped_image)

      new_label_file = os.path.join(output_folder, f"cropped_{i+1}_{image_file.replace('.jpg', '.txt')}")
      with open(new_label_file, "w") as f:
        for line in lines:
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            new_x_center = (x_center * image.shape[1] - x_start) / (x_end - x_start)
            new_y_center = (y_center * image.shape[0] - y_start) / (y_end - y_start)
            new_width = width * image.shape[1] / (x_end - x_start)
            new_height = height * image.shape[0] / (y_end - y_start)
            new_label = f"{int(class_id)} {new_x_center} {new_y_center} {new_width} {new_height}\n"
            f.write(new_label)

print("Image cropped and saved.")

