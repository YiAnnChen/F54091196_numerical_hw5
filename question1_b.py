import numpy as np
import matplotlib.pyplot as plt

# 定義 f(t, y)
def f(t, y):
    return 1 + (y / t) + (y / t) ** 2

# 定義 df/dt
def df_dt(t, y):
    term1 = -(y / t**2) - 2*(y**2) / (t**3)
    term2 = (1/t) + (2*y)/(t**2)
    return term1 + term2 * f(t,y)
# 真實解 y(t)
def exact_solution(t):
    return t * np.tan(np.log(t))


h = 0.1
T_start = 1.0
T_end = 2.0
t_values = np.arange(T_start, T_end + h, h)
y_values = []
y = 0  
y_values.append(y)


t_current = T_start
for i in range(1, len(t_values)):
    y = y + h * f(t_current, y) + (h**2)/2 * df_dt(t_current, y)
    y_values.append(y)
    t_current += h


y_exact = exact_solution(t_values)


errors = np.abs(np.array(y_values) - y_exact)


print(f"{'t':>5} {'Taylor y':>10} {'Exact y':>12} {'Error':>10}")
for i in range(len(t_values)):
    print(f"{t_values[i]:5.7f} {y_values[i]:10.7f} {y_exact[i]:12.5f} {errors[i]:10.7f}")





