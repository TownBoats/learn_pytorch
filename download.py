import os

# 安装you-get库
# pip install you-get

# 视频链接
video_url = "https://www.bilibili.com/video/BV1sN411Y7Ws"

# 下载视频
os.system(f"you-get {video_url}")