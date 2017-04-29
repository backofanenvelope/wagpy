# Basic program
import csv
import random

fname = 'carid.csv'

def csvtolist(fname):
    carlist = []
    with open(fname) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.__next__()
        for row in reader:
            carlist = list(reader)
        # print(carlist)
        return carlist

csvtolist(fname)

mycarlist = csvtolist(fname)
print(mycarlist)
