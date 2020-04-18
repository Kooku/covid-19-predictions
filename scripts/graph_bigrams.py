import matplotlib.pyplot as plt
import numpy as np

stayhome = np.cumsum(np.array([9, 29, 11, 11, 4, 74, 227, 355, 953, 1614, 913, 1264, 1540, 1764, 1227, 1772, 2354, 3007, 2864, 2949, 2612, 2420, 2998, 2041, 1895, 1795, 1707]))
x = np.array([i for i in range(0, len(stayhome))])

plt.plot(x, stayhome, label='stay home')
plt.legend()
plt.show()
