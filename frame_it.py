import cv2
import os

# 读取图片
result_folder = "crop2"
labels_folder = "crop2"
image_files = [filename for filename in os.listdir(result_folder) if filename.endswith(".jpg")]
class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

for image_file in image_files:
    # 读取图片
    image_path = os.path.join(result_folder, image_file)
    image = cv2.imread(image_path)

    # 读取相应的标签文件
    label_file = os.path.join(labels_folder, image_file.replace(".jpg", ".txt"))
    with open(label_file, "r") as f:
        lines = f.readlines()
  
    bounding_boxes = []
    annotated_image = image.copy()
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.strip().split())
        class_id = int(class_id)
        class_name = class_names[class_id]

        x_min = int((x_center - width / 2) * image.shape[1])
        y_min = int((y_center - height / 2) * image.shape[0])
        x_max = int((x_center + width / 2) * image.shape[1])
        y_max = int((y_center + height / 2) * image.shape[0])
        color = (0, 255, 0)  # 边界框的颜色为绿色
        cv2.rectangle(annotated_image, (x_min, y_min), (x_max, y_max), color, 2)
        label = f"{class_name}"
        cv2.putText(annotated_image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 显示带有绘制边界框和标签的图像
    cv2.imshow("带有边界框和标签的图像", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()







