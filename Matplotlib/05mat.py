#multiple plots in one figure
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return np.exp(-x) * np.cos(2 * np.pi * x)

t1=np.arange(0.0, 5.0, 0.1)
t2=np.arange(0.0, 5.0, 0.02)
plt.figure(1)
plt.subplot(211)#2 rows, 1 column, 1st plot
plt.grid()
plt.plot(t1, f(t1), '-b')
plt.subplot(212)#2 rows, 1 column, 2nd plot
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()