import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5)
y = x ** 2   # 幂函数
# 设置X轴标签
plt.xlabel("X值", size=15)
# 设置Y轴标签
plt.ylabel("Y值", size=15)
# 设置标题
plt.title("幂函数")
# 显示网格
plt.grid()
# 绘制图例
plt.plot(x, y, label="y=x2")
# 显示图例
plt.legend()
plt.show()