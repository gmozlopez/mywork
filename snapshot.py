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

def return_snapshots():
    snapshotlist = get_list_of_snapshots()
    getdates = get_dates()
    aDict = {}
    for sdate in getdates:
        #use get_dates to match on snapdaily else return an Autosync
        for snapshot in snapshotlist:
            if re.search(sdate, snapshot):
                aDict[sdate] = snapshot
    for dates, snapshot in sorted(aDict.items()):
        print "%s %s" % (dates,snapshot)

def return2arrays():
    snapshotlist2 = get_list_of_snapshots()
    getdates2 = get_dates()
    aDict = {}
    bDict = {}
    cDict = {}
    for sdate in getdates2:
        #use get_dates to match on snapdaily else return an Autosync
        for snapshot in snapshotlist2:
            if re.match("snap-daily", snapshot) and re.search(sdate, snapshot):
                aDict[sdate] = snapshot
            elif re.match("AutoSync", snapshot) and re.search(sdate, snapshot):
                bDict[sdate] = snapshot
    """
    for dates, asnapshot in sorted(aDict.items()):
        print "%s %s" % (dates,asnapshot)
    for dates, bsnapshot in sorted(bDict.items()):
        print "%s %s" % (dates,bsnapshot)
    """

    #for gdates in getdates2:
    #    print aDict[gdates]
    for sdate2 in getdates2:
        if sdate2 in aDict:
            cDict[sdate2] = aDict[sdate2]
        else:
            cDict[sdate2] = bDict[sdate2]

    for key, value in sorted(cDict.items()):
        print "%s, %s" % (key, value)



print return2arrays()