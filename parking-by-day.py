import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.axes as axes
import numpy as np

from functions import graph
from functions import add_key

filename = 'revenue-transaction-report-2011.csv'
lot_info_filename = 'lots.csv'
lf = open(lot_info_filename,'r')
# create a dictionary where the lot number is the key and the value is [name, total spaces, ID, address, half hour, coin cash, max, even, xcoord, ycoord]
lots = {}
for line in lf.readlines():
    myline = line.split(',')
    lots[myline[1]] = [myline[0], myline[2], myline[3], myline[5], myline[6], myline[7], myline[8], myline[9]]

initial = True
exittime = 0
entrytime = 0

legend = []
xAxis = ['0'] * minutes_in_a_day

datetimeformat4 = '%m/%d/%Y %H:%M'
datetimeformat2 = '%m/%d/%y %H:%M'

byLot = {}
lot = '0'
i = 0
with open(filename, 'r') as f:
    for i, line in enumerate(f):
        if initial:
            initial = False
        else:
            myline = line.split(',')
            entry = myline[0]
            lot = myline[4]

            if entry:
                try:
                    exittime = dt.datetime.strptime(myline[1], datetimeformat4)
                    entrytime = dt.datetime.strptime(entry, datetimeformat4)
                except:
                    exittime = dt.datetime.strptime(myline[1], datetimeformat2)
                    entrytime = dt.datetime.strptime(entry, datetimeformat2)                    
                entryminutes = entrytime.hour * 60 + entrytime.minute
                exitminutes = exittime.hour * 60 + exittime.minute
                if (i % 100000) == 0:
                    print("On line: " + str(i))


                if entryminutes > exitminutes:
                    # entered before midnight, left after midnight
                    for x in range(entryminutes, minutes_in_a_day):
                        byLot = add_key(byLot, entrytime.strftime('%A'), lot)
                        byLot[entrytime.strftime('%A')][lot][x] += 1
                    for x in range(0, exitminutes):
                        byLot = add_key(byLot, exittime.strftime('%A'), lot)
                        byLot[exittime.strftime('%A')][lot][x] += 1
                else:
                    for x in range(entryminutes,exitminutes):
                        byLot = add_key(byLot, entrytime.strftime('%A'), lot)
                        byLot[entrytime.strftime('%A')][lot][x] += 1

graph(byLot, lots)

