import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('develop.png')
 # 이미지를 읽어와서 img 변수에 저장함
 
plt.imshow(img)
plt.show()
 # 이미지를 출력해서 보여줌