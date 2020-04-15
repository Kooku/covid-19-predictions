import matplotlib.pyplot as plt
import numpy as np

stay_home_all = np.cumsum(np.array([6261, 8606, 7617, 5915, 7947, 7795, 7552, 7276, 8039, 6817, 7048, 7116, 7294, 7334, 6777, 5780, 5697, 5347, 5898, 7252, 6583, 5650, 5877]))
covid_19 = np.array([63056, 79421, 85876, 85937, 120843, 125985, 109444, 110352, 130436, 133508, 134128, 136656, 139627, 137354, 134274, 154076, 157280, 162077, 173752, 161344, 143263, 156727, 191641])
stay_home =  np.array([4573, 5777, 5489, 4356, 5796, 5719, 5440, 5294, 5979, 5130, 5271, 4996, 5430, 5601, 5277, 4482, 4474, 4239, 4184, 4998, 4665, 4546, 4431])
cum_covid_19 = np.cumsum(covid_19)
cum_stay_home = np.cumsum(stay_home)
dates = np.array([x for x in range(0,23)])

# m, b = np.polyfit(dates, cum_stay_home, 1)

plt.plot(dates, stay_home_all, label='stay home')
# plt.plot(dates, cum_covid_19, label='covid 19')
# plt.plot(dates, m*dates + b, label='Best fit line')
plt.legend()
plt.show()
