import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.axes as axes

filename = 'revenue-transaction-report-2011.csv'
lot_info_filename = 'lots.csv'
lf = open(lot_info_filename,'r')
# create a dictionary where the lot number is the key and the value is [name, total spaces, ID, address, half hour, coin cash, max, even, xcoord, ycoord]
lots = {}
for line in lf.readlines():
    myline = line.split(',')
    lots[myline[1]] = [myline[0],myline[2],myline[3],myline[5],myline[6],myline[7],myline[8],myline[9],myline[10],myline[11]]
                       

# f = open ( filename,'r')

# lines = f.readlines()

initial = True
exittime = 0
entrytime = 0
# numrecords = len(lines) - 1

minutes_in_a_day = 24*60

missing_lots = [10,12,14,3]

legend = []
xAxis = ['0']*minutes_in_a_day

byLot = {}
lot = '0'
i = 0
with open(filename,'r') as f:
    for i,line in enumerate(f):
        if initial:
            initial = False
        else:
            myline = line.split(',')
            entry = myline[0]
            lot = myline[4]

            if lot in missing_lots:
                print "Lot " + lots + " Has data."
            if entry:
                exittime = dt.datetime.strptime(myline[1], '%m/%d/%Y %H:%M')
                entrytime = dt.datetime.strptime(entry, '%m/%d/%Y %H:%M')
                if (i%100000) == 0:
                    print "On line: " + str(i)
                for x in range(entrytime.hour*60 + entrytime.minute,exittime.hour*60 + exittime.minute):
                    if lot not in byLot.keys():
                        byLot[lot] = [0]*minutes_in_a_day
                    byLot[lot][x] += 1
            elif lot in missing_lots:
                print "Lot " + str(lot) + "has no entry time"

suffix = 'AM'
for i,zero in enumerate(xAxis):
    if i/60.0 >= 12:
        suffix = ' PM'
    xAxis[i] = str(i/60.0)

today = dt.datetime.now()
times = [today + dt.timedelta(minutes=i) for i in range(minutes_in_a_day)]

plt.xlabel('Military Time (hours)')
plt.ylabel('Number of Cars Parked')
plt.title('Cars Parked During a Typical Day in 2011')

for key,value in byLot.iteritems():
    for i,v in enumerate(value):
        value[i] = v/256
    plt.plot(xAxis,value)
    print lots[key][0]
    legend.append(unicode(lots[key][0]))

plt.legend(legend, loc=2, borderaxespad=0.)

print "Number of lots: " + str(len(lots.keys()))
print "Number with 2011 data: " + str(len(legend))

print "Lots not graphed: "
for lot in lots.keys():
    if lots[lot][0] not in legend:
        print "Lot ID: " + str(lot)
        print "Lot Name: " + lots[lot][0]

plt.show()


