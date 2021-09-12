import numpy as np
import matplotlib.pyplot as plt

def step_fuction(x):
    return np.array(x>0, dtype=np.int)
 # 결과는 Bool 형태이므로 int형으로 변환

x = np.arange(-5.0, 5.0, 0.1)
 # x축의 범위는 -5.0부터 5.0까지, 간격은 0.1
y = step_fuction(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
 # y축의 범위 지정
plt.show()


