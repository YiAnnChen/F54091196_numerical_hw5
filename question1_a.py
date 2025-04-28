import numpy as np
import matplotlib.pyplot as plt

# 定義 f(t, y)
def f(t, y):
    return 1 + (y / t) + (y / t) ** 2

# 真實解 y(t)
def exact_solution(t):
    return t * np.tan(np.log(t))

# 初始化
h = 0.1
T_start = 1.0
T_end = 2.0
t_values = np.arange(T_start, T_end + h, h)
y_values = []
y = 0  
y_values.append(y)

# Euler's Method 計算
t_current = T_start
for i in range(1, len(t_values)):
    y = y + h * f(t_current, y)
    y_values.append(y)
    t_current += h

# 計算真實解
y_exact = exact_solution(t_values)

# 計算誤差
errors = np.abs(np.array(y_values) - y_exact)

# 顯示結果表格
print(f"{'t':>5} {'Euler y':>10} {'Exact y':>12} {'Error':>10}")
for i in range(len(t_values)):
    print(f"{t_values[i]:5.2f} {y_values[i]:10.5f} {y_exact[i]:12.5f} {errors[i]:10.5f}")