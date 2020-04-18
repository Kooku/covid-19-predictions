import matplotlib.pyplot as plt
import numpy as np

stayhome = np.cumsum(np.array([9, 29, 11, 11, 4, 74, 227, 355, 953, 1614, 913, 1264, 1540, 1764, 1227, 1772, 2354, 3007, 2864, 2949, 2612, 2420, 2998, 2041, 1895, 1795, 1707]))
social_distancing = np.cumsum(np.array([2, 6, 5, 2, 6, 41, 357, 786, 1130, 2417, 1896, 3689, 3352, 4382, 3033, 4659, 4341, 5313, 4557, 4302, 3214, 3553, 4292, 3028, 2635, 2575, 2556]))
covid19_socialdistancing = np.cumsum(np.array([0,0,0,0,0,2, 13, 71, 220, 205, 218, 338, 409, 594, 468, 740, 552, 793, 647, 711, 407, 460, 542, 333, 351, 452, 375]))
x = np.array([i for i in range(0, len(stayhome))])

plt.plot(x, stayhome, label='stay home')
plt.plot(x, social_distancing, label='social distancing')
plt.plot(x, covid19_socialdistancing, label='covid19_socialdistancing')
plt.legend()
plt.show()
