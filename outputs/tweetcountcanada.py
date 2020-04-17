import matplotlib.pyplot as plt
from itertools import accumulate


f = open("tweetcountcanada.txt", "r")
x_coordinates = []
y_coordinates = []
for line in f:
  arr = line[1:-2].split(",")
  y_coordinates.append(arr[0][-2:])
  print(arr[0][-2:])
  x_coordinates.append(int(arr[1]))


plt.plot(y_coordinates, list(accumulate(x_coordinates)))
plt.xlabel('Day in March')
plt.ylabel('Tweet Count in Canada')

plt.show()
