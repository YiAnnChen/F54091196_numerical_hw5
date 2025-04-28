import numpy as np
import matplotlib.pyplot as plt



def f1(t, u1, u2):
    return 9 * u1 + 24 * u2 + 5 * np.cos(t) - (1/3) * np.sin(t)

def f2(t, u1, u2):
    return -24 * u1 - 52 * u2 - 9 * np.cos(t) + (1/3) * np.sin(t)



def u1_exact(t):
    return 2 * np.exp(-3 * t) - np.exp(-39 * t) + (1/3) * np.cos(t)

def u2_exact(t):
    return -np.exp(-3 * t) + 2 * np.exp(-39 * t) - (1/3) * np.cos(t)

# Runge-Kutta 4階方法

def runge_kutta_system(h, T_end=1.0):
    t_values = np.arange(0, T_end + h, h)
    u1_values = []
    u2_values = []
    u1 = 4/3  
    u2 = 2/3
    u1_values.append(u1)
    u2_values.append(u2)

    for t in t_values[:-1]:
        k1_1 = f1(t, u1, u2)
        k1_2 = f2(t, u1, u2)

        k2_1 = f1(t + h/2, u1 + h/2 * k1_1, u2 + h/2 * k1_2)
        k2_2 = f2(t + h/2, u1 + h/2 * k1_1, u2 + h/2 * k1_2)

        k3_1 = f1(t + h/2, u1 + h/2 * k2_1, u2 + h/2 * k2_2)
        k3_2 = f2(t + h/2, u1 + h/2 * k2_1, u2 + h/2 * k2_2)

        k4_1 = f1(t + h, u1 + h * k3_1, u2 + h * k3_2)
        k4_2 = f2(t + h, u1 + h * k3_1, u2 + h * k3_2)

        u1 = u1 + h/6 * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)
        u2 = u2 + h/6 * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)

        u1_values.append(u1)
        u2_values.append(u2)

    return t_values, np.array(u1_values), np.array(u2_values)

for h in [0.1, 0.05]:
    print(f"\nStep size h = {h}")
    t_vals, u1_vals, u2_vals = runge_kutta_system(h)
    u1_true = u1_exact(t_vals)
    u2_true = u2_exact(t_vals)
    error_u1 = np.abs(u1_vals - u1_true)
    error_u2 = np.abs(u2_vals - u2_true)

    print(f"{'t':>5} {'u1 (RK4)':>12} {'u1 (Exact)':>12} {'Error u1':>10} | {'u2 (RK4)':>12} {'u2 (Exact)':>12} {'Error u2':>10}")
    for i in range(len(t_vals)):
        print(f"{t_vals[i]:5.2f} {u1_vals[i]:12.5f} {u1_true[i]:12.5f} {error_u1[i]:10.5e} | {u2_vals[i]:12.5f} {u2_true[i]:12.5f} {error_u2[i]:10.5e}")

   
