Issues
--------
There are some discrepencies with the data at this time so drawing conclusions other than general usage patterns is advised against.
Some issues include:
entry/exit times that are the same or just one minute apart
missing entry times

Features
--------
Currently it prints the following type of graph. The screenshot below treats all days as the same.

The parking-by-day script generates this graph for each day of the week. For images, check out the docs directory.

![screenshot](https://raw.github.com/friendlycode/grparking/master/docs/Typical%20Day.png)

Dependencies:
--------
Python (tested with 2.7)

matplotlib

The data at http://data.grcity.us/dataset/parking-ramp-transactions saved as csv files

The lots.csv file (recently added to github)

The script will take a while to process as it's going over a large amount of data.

