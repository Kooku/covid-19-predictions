import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit
from scipy.optimize import fsolve

def log_curve(x, k, x_0, ymax):
    return ymax / (1 + np.exp(-k*(x-x_0)))

y = [8, 8, 8, 8, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15, 20, 24, 27, 30, 34, 37, 54, 60, 66, 77, 95, 110, 142, 198, 252, 341, 441, 598, 727, 873, 1087, 1328, 1470, 2091, 2792, 3409, 4043, 4757, 5655, 6320, 7448, 8612, 9731, 11283, 12375, 13912, 15512, 16667, 17897, 19438, 20765, 22148, 23318, 24383, 25680, 27063, 28379, 30106, 31927]
x = np.array([x for x in range(0,len(y))])
popt, pcov = curve_fit(log_curve, x, y, p0=[0, 100, 50000])
estimated_k, estimated_x_0, ymax= popt

k = estimated_k
x_0 = estimated_x_0
x_prediction = np.array([x for x in range(0,len(y)+50)])
y_fitted = log_curve(x_prediction, k, x_0, ymax)
print('k, x_0 (inflection point), ymax')
print(k, x_0, ymax)

# errors
errors = [np.sqrt(pcov[i][i]) for i in [0,1,2]]
print(errors)

sol = int(fsolve(lambda x : log_curve(x, k, x_0, ymax) - int(ymax),k))
print('Will end {0} days from Feb 15.'.format(sol))

plt.plot(x, y, label='data')
plt.plot(x_prediction, y_fitted, '--', label='fitted')
plt.plot(sol, ymax, 'o', label='pandemic end')
plt.xlabel('x days from Feb 15')
plt.ylabel('number of confirmed cases in Canada')
plt.legend()
plt.show()
