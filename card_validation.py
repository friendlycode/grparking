from os import listdir
from os.path import isfile, join
import re

f_name = "card_data.csv"
f = open(f_name)

o_name = "card_data/"
match_inout_name = "good_card_data/"
unmatch_inout_name = "bad_card_data/"

split_into_files = False
if split_into_files is True:
    for line in f.readlines():
        files = listdir(o_name)
        myline = line.split(',')
        myid = myline[0]
        if myid in files:
            o = open(o_name+myid+".txt",'a+')
            o.write(line)
            o.close()
        else:
            o = open(o_name+myid+".txt",'w')
            o.write(line)
            o.close()
else:
    lot_num_index = 5
    matching_lot_nums = []
    non_matching_lot_nums = []
    for file in listdir(o_name):
        f = open(o_name + file)
        text = f.read()
        text = text.strip()
        lines = text.split('\n')
        ins = re.findall('In',text)
        outs = re.findall('Out',text)
        if len(ins) == len(outs):
            g = open(match_inout_name+file,'w')
            g.write(text)
            g.close()
            #print ("Matching # of ins and outs")
        else:
            b = open(unmatch_inout_name+file,'w')
            b.write(text)
            b.close()
            #print ("non-matching")
        f.close()

