import matplotlib.pyplot as plt
import numpy as np

coronavirus_response = [831, 145, 95, 197, 122, 170, 191, 177, 183, 312, 59, 56, 43, 73, 48, 58, 72, 62, 54, 67, 30, 25, 29, 88, 93, 73, 78, 40, 97, 47, 82, 38, 66, 35, 43]
fight_coronavirus = [853, 218, 184, 147, 118, 152, 104, 69, 62, 86, 23, 30, 22, 29, 17, 22, 21, 22, 17, 29, 19, 27, 20, 39, 28, 37, 28, 29, 74, 38, 43, 62, 88, 30, 66]
sign_petition = [1001, 1001, 1001, 1001, 348, 45, 32, 91, 165, 49, 41, 62, 36, 91, 53, 77, 55, 84, 71, 104, 48, 59, 81, 81, 119, 90, 169, 84, 121, 90, 137, 248, 203, 228, 258]
x = [x for x in range(0, len(coronavirus_response))]

plt.plot(x, coronavirus_response, label='coronavirus response')
plt.plot(x, fight_coronavirus, label='fight coronavirus')
plt.plot(x, sign_petition, label='sign petition')
plt.legend()
plt.show()
