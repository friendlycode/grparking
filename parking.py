import datetime as dt
import matplotlib.pyplot as plt
filename = 'revenue-transaction-report-2011.csv'
f = open ( filename,'r')

lines = f.readlines()

initial = True
exittime = 0
entrytime = 0
numrecords = len(lines) - 1

minutes = [0]*1440
count = [0]*1440

for i,line in enumerate(lines):
    if initial:
        initial = False
    else:
        myline = line.split(',')
        entry = myline[0]
        if entry:
            exittime = dt.datetime.strptime(myline[1], '%m/%d/%Y %H:%M')
            entrytime = dt.datetime.strptime(entry, '%m/%d/%Y %H:%M')
            for x in range(entrytime.hour*60 + entrytime.minute,exittime.hour*60 + exittime.minute):
                minutes[x] += 1

plt.plot(minutes)
plt.show()
