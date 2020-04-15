import matplotlib.pyplot as plt
import numpy as np

y = np.cumsum(np.array([6261, 8606, 7617, 5915, 7947, 7795, 7552, 7276, 8039, 6817, 7048, 7116, 7294, 7334, 6777, 5780, 5697, 5347, 5898, 7252, 6583, 5650, 5877]))
x = np.array([x for x in range(0,len(y))])

z = np.poly1d(np.polyfit(x, y, 3))

print('Prediction:')
predictions= []
for i in range(24, 34):
    predictions.append(z(i))

plt.plot(range(0, 10), predictions, label='predictions')
plt.legend()
plt.show()
