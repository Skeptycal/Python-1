from matplotlib import pyplot as plt
import numpy as np


xone = [1, 2, 3, 4, 5]
yone = [0, 5, 10, 15, 20]

xtwo = [1, 5]
ytwo = [10, 10]

t = np.arange(0.0, 2.0, 0.01)
s = np.cos(np.pi*t)

plt.figure(1)
plt.subplot(211)
plt.plot(t,s)

plt.figure(2)
plt.subplot(212)
plt.plot(xtwo, ytwo)

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()
