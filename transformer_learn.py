import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image


# 读取图片
image_path = 'data\Chapter3\狗狗2.jpg'
image = Image.open(image_path)

# 定义预处理转换
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),      # 调整图片尺寸
    transforms.ToTensor(),              # 将图片转为 Tensor 格式，并将像素值缩放到 [0, 1] 范围
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # 标准化
    transforms.RandomHorizontalFlip(p=0.9)
])

# 应用预处理转换
processed_image = preprocess(image)

# 将 Tensor 转换为 NumPy 数组，并反标准化像素值
unnormalized_image = transforms.Normalize(mean=[-0.485/0.229, -0.456/0.224, -0.406/0.225],
                                          std=[1/0.229, 1/0.224, 1/0.225])(processed_image)
numpy_image = unnormalized_image.numpy()
numpy_image = numpy_image.transpose((1, 2, 0))  # 调整维度顺序

# 展示图片
plt.imshow(numpy_image)
plt.axis('off')  # 关闭坐标轴
plt.show()


