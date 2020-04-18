import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit
from scipy.optimize import fsolve

def log_curve(x, k, x_0, ymax):
    return ymax / (1 + np.exp(-k*(x-x_0)))

# data =  np.array([9, 29, 11, 11, 4, 71, 221, 349, 943, 1603, 905, 1249, 1500, 1728, 1203, 1736, 2320, 2960, 5777, 5489, 4356, 5796, 5719, 5440, 5294, 5979, 5130, 5271, 4996, 5430, 5601, 5277, 4482, 4474, 4239, 4184, 4998, 4665, 4546, 4431, 4735, 3768])
# data =  np.array([18, 58, 22, 22, 8, 142, 442, 698, 1886, 3206, 1810, 2498, 3000, 3456, 2406, 3472, 4640, 5920, 5777, 5489, 4356, 5796, 5719, 5440, 5294, 5979, 5130, 5271, 4996, 5430, 5601, 5277, 4482, 4474, 4239, 4184, 4998, 4665, 4546, 4431, 4735, 3768])
# data = np.array([9, 29, 11, 11, 4, 71, 221, 349, 943, 1603, 905, 1249, 1500, 1728, 1203, 1736, 2320, 2960])
# data = np.array([6, 5, 10, 22, 6, 64, 216, 474, 2650, 2256, 907, 1632, 1176, 1598, 1086, 1740, 1031, 1036, 987, 992, 713, 1197, 1318, 1474, 1087, 1092, 650, 1198, 6337]) # canada
data = np.array([6, 5, 4, 4, 6, 40, 115, 300, 597, 545, 542, 485, 555, 803, 531, 777, 590, 710, 661, 538, 493, 544, 642, 602, 623, 542, 401, 561, 466]) # no retweets
y = np.cumsum(data)
x = np.array([x for x in range(0,len(y))])
popt, pcov = curve_fit(log_curve, x, y, p0=[0, 25, 30000])
estimated_k, estimated_x_0, ymax= popt

k = estimated_k
x_0 = estimated_x_0
x_prediction = np.array([x for x in range(0,len(y)+50)])
y_fitted = log_curve(x_prediction, k, x_0, ymax)
print(k, x_0, ymax)

# errors
errors = [np.sqrt(pcov[i][i]) for i in [0,1,2]]
print(errors)

sol = int(fsolve(lambda x : log_curve(x, k, x_0, ymax) - int(ymax),k))
print(sol)

plt.plot(x, y, label='data')
plt.plot(x_prediction, y_fitted, '--', label='fitted')
plt.xlabel('x days from March 1st')
plt.ylabel('number of "stay home" bigrams in tweets')
plt.legend()
plt.show()
