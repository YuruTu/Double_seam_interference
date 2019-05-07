##############
#利用python仿真双缝实验
#时间：2018/12/31
#作者：cclplus
#仅供学习交流使用
#如有疑问或者需求，可以联系作者707101557@qq.com

import numpy as np
import matplotlib.pyplot as plt
import math

#表示长度的物理量单位m
#波长
wavelength=float(5.0*10**-9)
#双缝间距
d_slit=float(0.002)
#缝到屏幕的距离
d_screen=float(1.0)

ym=5.0*wavelength*d_screen/d_slit
xs=ym
distance=ym/50.0
ys=np.arange(-ym,ym,distance)
len_dis=len(ys)
B = [([0.0] * len_dis) for i in range(len_dis)]
Br = [([0.0] * len_dis) for i in range(len_dis)]
N=255.0
for i in range(0,len_dis):
    r1=math.sqrt((ys[i]-d_slit/2)**2+d_screen**2)
    r2=math.sqrt((ys[i]+d_slit/2)**2+d_screen**2)
    phi=2.0*math.pi*(r2-r1)/wavelength
    temp=4.0*math.cos(phi/2)**2
    for j in range(0,len_dis):
        B[i][j]=temp
        Br[i][j]=B[i][j]/4.0*N

plt.title("double_slit_experiment")
plt.imshow(Br, cmap='gray')
plt.show()
