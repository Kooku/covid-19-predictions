import csv
from collections import defaultdict

dates = defaultdict(lambda:0)

with open('covid19.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] == 'Canada':
            dateString = row[3][3:5] + '-' + row[3][:2]
            dates[dateString] = row[12]

print(dates)
