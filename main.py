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
        f[j][i] = i*h+2*j*t-exp(i*h)-a*(12*(i*h)**2-j*t*exp(i*h))









