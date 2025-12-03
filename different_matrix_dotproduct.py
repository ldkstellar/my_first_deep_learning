import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])  # 2*3 행렬

b = np.array([[10, 11], [20, 21], [30, 31]])  # 3*2 행렬


# 트랜스 포스(전치행렬)라는 행과 열을 바꾸는 메소드가 있다. 값이 바뀌어짐
print(b.T)
a_matmul_b = np.matmul(a, b)
a_at_b = a @ b

print(a_matmul_b)
print(a_at_b)
