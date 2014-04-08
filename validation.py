
import datetime as dt

def is_timedif_an_event(entry_time, exit_time):
    if ( divmod((exit_time-entry_time).total_seconds(),60)[0] < 5 ):
        return True
    else:
        return False

def is_timedif_greater_than_hours(entry_time, exit_time, hours):
    if ( divmod((exit_time-entry_time).total_seconds(),60*60)[0] > hours ):
        return True
    else:
        return False

def got_no_money(cash_value):
    cash = float(cash_value.replace('$','').replace("\"",""))
    if cash > 0:
        return False
    else:
        return True
filename = 'revenue-transaction-report-2011.csv'
f = open(filename,'r')
lines = f.readlines()
f.close()

initial = True 

datetimeformat4 = '%m/%d/%Y %H:%M'
datetimeformat2 = '%m/%d/%y %H:%M'

time_for_no_money = dt.datetime.now() - dt.datetime.now()
time_started_for_no_money = None
num_events_per_lot = {}
lot_daysparked_numcars = {}
for line in lines:
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
            entryminutes = entrytime.hour*60 + entrytime.minute
            exitminutes = exittime.hour*60 + exittime.minute

            difftime = exittime - entrytime
            # print ( difftime )
            if got_no_money(myline[2]) and difftime > time_for_no_money:
                time_for_no_money = difftime
                time_started_for_no_money = entrytime
                #print ( "No money for " + str(difftime) + " diff time.")
            if is_timedif_an_event(entrytime,exittime):
                if lot in num_events_per_lot.keys():
                    num_events_per_lot[lot] += 1
                else:
                    num_events_per_lot[lot] = 1
            if is_timedif_greater_than_hours(entrytime,exittime,24):
                days_parked = difftime.days
                if lot in lot_daysparked_numcars.keys():
                    if days_parked in lot_daysparked_numcars[lot].keys():
                        lot_daysparked_numcars[lot][days_parked] += 1
                    else:
                        lot_daysparked_numcars[lot][days_parked] = 1                            
                else:
                    lot_daysparked_numcars[lot] = {}
                    lot_daysparked_numcars[lot][days_parked] = 1
longest_stay = (0,dt.datetime.today()-dt.datetime.today())

print ( "longest time for no money is " + str(time_for_no_money) + " started at " + str(time_started_for_no_money))

for key in num_events_per_lot.keys():
    print ( "Lot " + str(key) + " had " + str(num_events_per_lot[key]) + " event tickets sold ")

for lot in lot_daysparked_numcars.keys():
    for daysparked in lot_daysparked_numcars[lot]:
        print ( "Lot " + str(lot) + " num days parked " + str(daysparked) + " Number of units " + str(lot_daysparked_numcars[lot][daysparked]))

                    


