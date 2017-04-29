# Basic program
import csv
import random

fname = 'carid.csv'

def csvtolist(fname):
    with open(fname) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.__next__()
        for row in reader:
            carlist = list(reader)
        print(carlist)

csvtolist(fname)
