import matplotlib.pyplot as plt
import numpy as np
f = open('LAB4.2.10.txt', 'r', encoding="utf-8")

X = list(map(int, f.readline().strip().split()[1:]))
Y = list(map(int, f.readline().strip().split()[1:]))

print(X, Y)
fig, ax = plt.subplots()
ax.plot(X, Y)
plt.show()
