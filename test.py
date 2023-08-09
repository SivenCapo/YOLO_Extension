import cv2
import os

def extract_frames(input_video, output_directory, interval=2):
    # 打开视频文件
    cap = cv2.VideoCapture(input_video)

    # 确保视频文件打开成功
    if not cap.isOpened():
        print("Error: 无法打开视频文件。")
        return

    # 获取视频的帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 计算间隔的帧数
    interval_frames = fps * interval

    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    frame_count = 0

    while True:
        # 读取视频的帧
        ret, frame = cap.read()

        # 判断是否到达视频结尾
        if not ret:
            break

        frame_count += 1

        # 每隔两秒保存一帧
        if frame_count % interval_frames == 0:
            output_path = os.path.join(output_directory, f"frame_{frame_count // interval_frames}.jpg")
            cv2.imwrite(output_path, frame)

    cap.release()
    print("视频帧提取完成。")

# 使用示例
input_video = "2.mp4"  # 输入视频文件路径
output_directory = "output1"  # 输出帧的目录
interval = 10  # 间隔时间（单位：秒）

extract_frames(input_video, output_directory, interval)
