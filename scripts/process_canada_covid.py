import csv
import numpy as np
from collections import defaultdict

dates = defaultdict(lambda:0)

with open('covid19.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] == 'Canada':
            dateString = row[3][3:5] + '-' + row[3][:2]
            dates[dateString] = row[12]

dates = {k: v for k, v in dates.items() if v is not None and v != ''}
print(dates)

values = []
for key, value in dates.items():
    values.append(int(value))

values = np.array(values)
values = np.cumsum(values)

i = 0
for key, value in dates.items():
    print('{}: {}'.format(key, values[i]))
    i += 1

