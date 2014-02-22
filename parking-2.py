import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as md

filename = 'revenue-transaction-report-2011.csv'
f = open ( filename,'r')

lines = f.readlines()

initial = True
exittime = 0
entrytime = 0
numrecords = len(lines) - 1

minutes = [0]*1440
count = [0]*1440

byLot = {}

for i,line in enumerate(lines):
    if initial:
        initial = False
    else:
        myline = line.split(',')
        entry = myline[0]
        lot = myline[4]
        if entry:
            exittime = dt.datetime.strptime(myline[1], '%m/%d/%Y %H:%M')
            entrytime = dt.datetime.strptime(entry, '%m/%d/%Y %H:%M')
#            print lot
            for x in range(entrytime.hour*60 + entrytime.minute,exittime.hour*60 + exittime.minute):
                if lot not in byLot.keys():
                    byLot[lot] = [0]*1440
                byLot[lot][x] += 1
                # minutes[x] += 1

#print "For lot: " + byLot.keys()[0]
#print byLot[byLot.keys()[0]]

#print "Lots in dictionary are: "
#print byLot.keys()

#print byLot

for key,value in byLot.iteritems():
    plt.plot(value)


plt.legend(byLot.keys())
    
plt.show()
