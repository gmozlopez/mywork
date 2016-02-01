import sys
import os
import re

mount = sys.argv[1]
files = os.listdir(mount)

def get_list_of_snapshots():
    snapshot_arr = []
    for names in files:
        if re.search("(\d{4}\-\d{2}\-\d{2})", names):
            snapshot_arr.append(names)
    return snapshot_arr

def get_dates():
    datelist = []
    snapshots = get_list_of_snapshots()
    for dates in snapshots:
        date1 = re.split("(\d{4}-\d{2}-\d{2})", dates)[1]
        datelist.append(date1)
    return set(datelist)

mylist = get_list_of_snapshots()
getdates = get_dates()
for dates in getdates:
	y = []	
	for ylist in mylist:
		if re.search(dates, ylist):
			y.append(ylist)
	print y


			