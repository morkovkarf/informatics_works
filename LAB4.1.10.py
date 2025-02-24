import matplotlib.pyplot as plt
import numpy as np
a=float(input())
b=float( input())
c=float( input())
print("Введите диапазон (от, до, количесвто точек)")
dbeg=int( input())
dend=int( input())
dprom=int( input())

if dbeg>0:
    x = np.linspace(dbeg, dend, dprom)
    y =a+b*x**2+c*x**(1/2)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
else:
    print("error")
