import numpy as np
import matplotlib . pyplot as plt

# Parameters and initialization

i0 =0.001
ip =0.005
import math

# Initial conditions
H0 =1.5
g = 9.81
dt =0.1
dx = 0.2
r = dt / dx
Nt = 10
Nx = 10
A = 1
B = 1
D = 5
nu = 0.03

# Vectors Initialization
H = np.zeros(Nx, dtype=float)
V = np.zeros(Nx, dtype=float)

Hs = np.empty((Nx, Nx))
Vs = np.empty((Nx, Nx))

# Schemas
for n in range(Nt - 1):
    H_i = np.copy(H)
    V_i = np.copy(V)

    for i in range(Nx - 1):
        if n == 0:
            beta = 1 - (2 * H0 / D)
            bo = D * np.sqrt(1 - beta ** 2)
            R = D / 4 * (1 - (beta * np.sqrt(1 - beta ** 2) / math.acos(beta)))
            Cw = R ** (1/6) / nu
            x = 10 + (12 * H0 / bo) / (3 + (6 * H0 / bo))
            vo = Cw * np.sqrt(i0 * R)
            
            a = Cw - vo
            b = 2 * Cw - (x * vo)
            A = 2 * (a * H0) - (H0 * vo) / b
            B = H0 - A
            c = -1 * g * i0 * b / (vo * g * H0 - a ** 2)
            C = np.exp(c * (i / Nx))
            H_i[i] = A + (B * C)
            V_i[i] = 1 / H0 * a * (H_i[i] - H0) + vo
        else:
            H_i[i] = H[i] - (r) * ((V[i] * (H[i + 1] - H[i])) - (A / B) * r * (V[i + 1] - V[i]))
            V_i[i] = V[i] - (r) * (V[i] * (V[i + 1] - V[i])) - (g * r) * (H[i + 1] - H[i]) + dt * g * (i0 - ip)
        
        H[i] = H_i[i]
        V[i] = V_i[i]

    H = H_i
  print(H_i[i], V_i[i])
Hs[n, :] = H_i
Vs[n, :] = V_i

plt.figure(figsize=(10, 6))
for ii in range(Hs.shape[0]):
    plt.plot(Hs[ii, :], label=f"Ligne {ii + 1}")
    # plt.legend()
plt.xlabel('Position')
plt.ylabel('Section Transversale H')
plt.title('Courbe de niveau d\'eau')
plt.grid(True)
plt.show()

# Visualization of speed (V) evolution over time
plt.figure(figsize=(10, 6))
for ii in range(Vs.shape[0]):
    plt.plot(Vs[ii, :], label=f"Ligne {ii + 1}")

plt.xlabel('Position')
plt.ylabel('Vitesse (V)')
plt.title('Courbe de Vitesse')
plt.grid(True)
plt.show()

