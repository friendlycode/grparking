from os import listdir
from os.path import isfile, join

f_name = "card_data.csv"
f = open(f_name)

o_name = "card_data/"

for line in f.readlines():
    files = listdir(o_name)
    myline = line.split(',')
    myid = myline[0]
    if myid in files:
        o = open(o_name+myid,'a+')
        o.write(line)
        o.close()
    else:
        o = open(o_name+myid,'w')
        o.write(line)
        o.close()
    
