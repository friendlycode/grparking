

f_name = "2013 Card Activity.csv"
f = open(f_name)

c_name = "card_data.csv"
v_name = "building_data.csv"

cfile = open(c_name,'w')
vfile = open(v_name,'w')

for line in f.readlines():
    if "Neutral" in line:
        vfile.write(line)
    else:
        cfile.write(line)        
