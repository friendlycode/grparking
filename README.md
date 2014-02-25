grparking scripts came out of the code across gr event.
parking.py was our initial graph which just takes all the entry and exit data from the 2011 document here: http://data.grcity.us/dataset/parking-ramp-transactions and treats it all as one lot on one day.
parking-2.py is our second graph which graphs a typical day for each lot.

Some Likely Future Additions:
a modification to either the data or code so that the code can process the year for both 2011 and 2012
a script that plots % usage for each lot for each day of the week (different plots for each day with all the lots for that day on them)
a way to correlate high usage to specific events and determine how far away people are parking for each event
a better x-axis so that it has a tick for every hour
some sort of graph over all the data sets
speed-ups for parsing data?

Dependencies:
Python (tested with 2.7)
matplotlib
The data at http://data.grcity.us/dataset/parking-ramp-transactions saved as csv files
The lots.csv file (currently not publicly available, need to talk to Traci about this)

The script will take a while to process as it's going over a large amount of data.

