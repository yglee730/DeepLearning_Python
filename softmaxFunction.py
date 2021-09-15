import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
     # 오버플로우를 방지하기 위해 가장 큰 수를 뺀다
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

a = np.array([0.3, 4.0, 2.9])
y = softmax(a)

print(y)

print("y 합 :",np.sum(y))