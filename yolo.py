import cv2
import os

# 读取图片
result_folder = "crop3"
labels_folder = "crop3"
output_folder = "cropped_images"
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
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.strip().split())
        class_id = int(class_id)
        class_name = class_names[class_id]

        x_min = int((x_center - width / 2) * image.shape[1])
        y_min = int((y_center - height / 2) * image.shape[0])
        x_max = int((x_center + width / 2) * image.shape[1])
        y_max = int((y_center + height / 2) * image.shape[0])

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        #cropped_image = image[y_min:y_max, x_min:x_max]

        # class_folder = os.path.join(output_folder, class_name)
        # os.makedirs(class_folder, exist_ok=True)

        # # 保存裁剪后的图片
        # cropped_image_path = os.path.join(class_folder, image_file)
        # cv2.imwrite(cropped_image_path, cropped_image)
    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(1000)  # 显示图片1秒
    cv2.destroyAllWindows()



# 显示绘制了边界框和类别标签的图片
