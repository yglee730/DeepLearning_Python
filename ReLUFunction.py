import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
    return np.maximum(0, x)
 # 두 수를 비교해서 최댓값을 반환
 # 0보다 작으면 0이 출력되고 0보다 크면 그 수가 출력됨

x = np.arange(-3.0, 3.0, 0.1)
 # x축의 범위는 -3.0부터 3.0까지
 # 간격은 0.1에 범위는 -3.0부터 3.0까지인 배열 생성
 
y = ReLU(x)

plt.plot(x, y)
plt.ylim(-0.1, 3.1)
 # y축의 범위 지정
 
plt.show()


