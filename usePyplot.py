import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
 # 0부터 6까지 0.1 간격으로 칸 생성
 
y1 = np.sin(x)
 # sin 그래프를 y1 변수에 저장 
 
y2 = np.cos(x)
 # cos 그래프를 y2 변수에 저장

plt.plot(x, y1, label="sinGraph")
 # sinGraph라는 이름을 가진 그래프를 그림 

plt.plot(x, y2, linestyle="--", label="cosGraph")
 # cosGraph라는 이름을 가진 그래프를 "점선"으로 그림
 
plt.xlabel("x축")
 # x축의 이름은 "x축"
 
plt.xlabel("y축") 
 # y축의 이름은 "y축"
 
plt.title('sin&cos')
 # 전체 그래프의 제목은 "sin&cos"
 
plt.legend()
 # 그래프의 범례 표시
 # 범례 -> 데이터의 종류를 표시하기 위한 텍스트
 
plt.show()
 # 그래프를 화면으로 보여줌

