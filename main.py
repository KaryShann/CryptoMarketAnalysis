import csv

with open('data/Bitcoin - Bitcoin.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

print("Hello, world!")