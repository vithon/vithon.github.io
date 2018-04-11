# encoding: utf-8
from matplotlib import pyplot as plt

xs = [-2, -1, 0, 1]
ys = [0, -3, -4, -3]

plt.plot(xs, ys, 'bo')
plt.plot([x / 100.0 for x in range(min(xs) * 100, max(xs) * 100)],
         [(x / 100.0)**2 - 4.0
          for x in range(min(xs) * 100, max(xs) * 100)],
         'g--')
plt.savefig('linear-reg-4.png')

# Bảng đầu vào.
xs = [(1, -2, 4), (1, -1, 1), (1, 0, 0), (1, 1, 1)]  # (x_0, x_1, x_2)
ys = [0, -3, -4, -3]  # y

# Khởi tạo theta là vec tơ (0, 0, 0).
theta = [0] * len(xs[0])
# Định tốc độ học.
alpha = 0.01

# Điều kiện hội tụ là lặp 10000 lần.
for _ in range(10000):
  theta_new = [0] * len(theta)
  for j in range(len(theta)):
      # Tính độ dốc theo theta_j.
      gradient = 0
      for i in range(len(ys)):
          y_hat = (theta[2] * xs[i][2] +
                   theta[1] * xs[i][1] +
                   theta[0] * xs[i][0])
          gradient += (ys[i] - y_hat) * xs[i][j]
      # Cập nhật theta.
      theta_new[j] = theta[j] + alpha * gradient
  theta = theta_new
print(theta)
