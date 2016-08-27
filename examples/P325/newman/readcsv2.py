import csv
import matplotlib.pyplot as plt

data = csv.reader(open('drop.dat', 'r'), delimiter=" ", quotechar='"')
column1, column2 = [], []

for row in data:
    column1.append(float(row[0]))
    column2.append(float(row[1]))

plt.plot(column1,column2)
plt.show()
