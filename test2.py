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
    print(fps)

    # 计算间隔的帧数
    interval_frames = fps * interval






    cap.release()
    print("视频帧提取完成。")

# 使用示例
input_video = "1.mp4"  # 输入视频文件路径
output_directory = "output1"  # 输出帧的目录
interval = 2  # 间隔时间（单位：秒）

extract_frames(input_video, output_directory, interval)
