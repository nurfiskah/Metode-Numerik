
import numpy as np

def f(x):
    return x*e**(-x)+np.cos(2*x)

err = 10**(-14)
x = np.zeros(1)
x[0] = 1
x[1] = 3

for n in range (1,13):
    x[n+1] = x[n] - f(x[n])*(x[n] - x[n-1])/(f(x[n]) - f(x[n-1]))
    print(n+1,x[n+1],f(x[n+1]))
    if abs(f(x[n])) < err:
        break