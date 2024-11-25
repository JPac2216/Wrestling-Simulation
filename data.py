import csv

with open('wwemen.csv', mode='r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]