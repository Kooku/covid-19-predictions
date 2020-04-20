import matplotlib.pyplot as plt
import numpy as np

coronavirus_response = np.array([831, 145, 95, 197, 122, 170, 191, 177, 183, 312, 59, 56, 43, 73, 48, 58, 72, 62, 54, 67, 30, 25, 29, 88, 93, 73, 78, 40, 97, 47, 82, 38, 66, 35, 43])
delta_corona = np.diff(coronavirus_response)
fight_coronavirus = [853, 218, 184, 147, 118, 152, 104, 69, 62, 86, 23, 30, 22, 29, 17, 22, 21, 22, 17, 29, 19, 27, 20, 39, 28, 37, 28, 29, 74, 38, 43, 62, 88, 30, 66]
sign_petition = [1001, 1001, 1001, 1001, 348, 45, 32, 91, 165, 49, 41, 62, 36, 91, 53, 77, 55, 84, 71, 104, 48, 59, 81, 81, 119, 90, 169, 84, 121, 90, 137, 248, 203, 228, 258]
delta_sign = np.diff(np.array(sign_petition))
fight_covid = [35, 43, 15, 26, 73, 125, 119, 58, 47, 42, 172, 113, 99, 99, 80, 78, 58, 66, 69, 107, 62, 64, 47, 86, 65, 65, 43, 37, 85, 67, 62, 82, 118, 68, 74]
delta_fight_corona = np.diff(np.array(fight_covid))
staying_home = [726, 703, 543, 239, 279, 284, 334, 302, 221, 144, 212, 190, 152, 201, 168, 151, 173, 191, 147, 191, 198, 219, 123, 173, 188, 168, 200, 198, 262, 166, 217, 296, 243, 339, 357]
x = [x for x in range(0, len(coronavirus_response))]
x_delta = [x for x in range(1, len(coronavirus_response))]

plt.plot(x, coronavirus_response, label='coronavirus response')
# plt.plot(x, fight_coronavirus, label='fight coronavirus')
plt.plot(x, fight_covid, label='fight covid')
plt.plot(x, sign_petition, label='sign petition')
plt.plot(x, staying_home, label='staying home')
# plt.plot(x_delta, delta_corona, '--', label='delta coronavirus response')
# plt.plot(x_delta, delta_fight_corona, '--', label='delta fight corona')
# plt.plot(x_delta, delta_sign, '--', label='delta sign petition')
plt.xlabel('x Days from March 12th')
plt.ylabel('Bigram Ranking')
plt.legend()
plt.show()
