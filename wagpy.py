# Basic program
import csv
import random

with open('carid.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
