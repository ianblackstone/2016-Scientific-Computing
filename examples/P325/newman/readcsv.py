import csv

data = csv.reader(open('drop.dat', 'r'), delimiter=" ", quotechar='"')
column1, column2 = [], []

for row in data:
    column1.append(row[0])
    column2.append(row[1])

print(column1)
print(column2)
