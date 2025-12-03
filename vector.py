import numpy as np

a = np.array([1, 2, 3])  # 1차원 배열
b = np.array([4, 5, 6])  # 2차원 배열

a_mu_b = a * b
a_dot_b = np.dot(a, b)  # 곱하기를 모두 따로 해서 더한다는의미가 dot product
a_at_b = a @ b  # dot이랑 똑같은 의미이다.
print(a_mu_b, end=" ")
print(a_dot_b, end=" ")
print(a_at_b)
