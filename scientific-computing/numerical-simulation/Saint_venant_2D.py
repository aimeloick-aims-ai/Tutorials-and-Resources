import numpy as np
import math
import matplotlib.pyplot as plt

t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8])
il = np.arange(0, 10, 1)

D = 5
io = 0.1
ho = 1.5
nu = 0.03
g = 9.8
Ho = ho

for i in range(len(t)):
    beta = 1 - (2 * ho / D)
    bo = D * np.sqrt(1 - beta ** 2)
    R = D / 4 * (1 - (beta * np.sqrt(1 - beta ** 2) / math.acos(beta)))
    Cw = R ** (1/6) / nu
    x = 10 + (12 * ho / bo) / (3 + (6 * ho / bo))
    vo = Cw * np.sqrt(io * R)
    z = Cw * t + il
    a = Cw - vo
    b = 2 * Cw - (x * vo)
    A = 2 * (a * Ho) - (ho * vo) / b
    B = Ho - A
    c = -1 * g * io * b / (vo * g * ho - a ** 2)
    C = np.exp(c * z)
    H = A + (B * C)
    V = 1 / ho * a * (H - Ho) + vo

    plt.plot(il, H, label=f'courbe de H pour t={t[i]}')
    plt.plot(il, V, label=f'courbe de V pour t={t[i]}')

plt.xlabel('Axe de x')
plt.ylabel('H et V')
plt.legend()
plt.show()
