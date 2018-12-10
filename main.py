import matplotlib.pyplot as plt
import numpy as np
from math import exp

h = 0.1
t = 0.1

a = 0.024

nx = int(1/h)+1
nt = int(1/t)+1

u = np.zeros((nt, nx))
f = np.zeros((nt, nx))
ru = np.zeros((nt, nx))

for i in range(0, nx):
    for j in range(0, nt):
        ru[j][i] = (i*h)**4+i*h*j*t+(j*t)**2-j*t*exp(i*h)

for i in range(0, nx):
    u[0][i] = (i*h)**4

for j in range(0, nt):
    u[j][0] = (j*t)**2-j*t

for j in range(0, nt):
    u[j][nx-1] = 1+j*t+(j*t)**2-t*j*exp(1)

for i in range(0, nx):
    for j in range(0, nt):
        f[j][i] = i*h+2*j*t-exp(i*h)-a*(12*((i*h)**2)-j*t*exp(i*h))

for j in range(1, nt):
    for i in range(1, nx-1):
        u[j][i] = u[j-1][i] + t*a/(h**2)*(u[j-1][i+1]+u[j-1][i-1]-2*u[j-1][i])+t*f[j-1][i]

b = u-ru
c = -(u-ru)

print(b.max())
print(c.max())

tt = np.arange(0, 1+t, t)

xx = np.arange(0, 1+h, h)

for i in range(0, 11):
    plt.figure(figsize=(20, 10))
    plt.subplot(1, 1,  1)
    plt.plot(xx, u[i * int(0.1 / t)], 'bo')
    plt.title('t = ' + str(i/10))
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.grid(True)
    plt.subplot(1, 1,  1)
    plt.plot(xx, ru[i * int(0.1 / t)], 'r+')
    plt.grid(True)
    plt.show()

plt.figure(figsize=(20, 10))
plt.subplot(1, 1,  1)
plt.plot(tt, u[:, int(0.5 / h)], 'bo')
plt.title('x = 0.5')
plt.xlabel('t')
plt.ylabel('Value')
plt.grid(True)
plt.subplot(1, 1,  1)
plt.plot(tt, ru[:, int(0.5 / h)], 'r+')
plt.grid(True)
plt.show()




