import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle
import sys

print('正在读取参数')
infile = sys.argv[1]
print('正在读取文件')
with open(infile, 'rb') as infile:
    lina = pickle.load(infile)
print('读取文件成功')
plt.imshow(lina)  # 显示图片
plt.axis('off')  # 不显示坐标轴
plt.show()
print('展示结束')
