import sys
import os
import re

mount = sys.argv[1]
files = os.listdir(mount)

def get_snapshots(name):
    snapshot_arr = []
    for snaps in files:
        if name in snaps:
            snapshot_arr.append(snaps)
    return snapshot_arr

def get_list_of_snapshots():
    snapshot_arr = []
    for names in files:
        if re.search("(\d{4}\-\d{2}\-\d{2})", names):
            snapshot_arr.append(names)
    return snapshot_arr

def split_file_names():
    snapdaily = []
    autosync = []
    snapshots = get_list_of_snapshots()
    for snap in snapshots:
        if re.match("snap-daily", snap):
            snapdaily.append(snap)
        elif re.match("AutoSync", snap):
            autosync.append(snap)
    dates = get_dates()
    for date in dates:
        for snapd in snapdaily:
            if re.search(date, snapd):
                #print snapd
                pass
            else:
                for autos in autosync:
                    if re.search(date, autos):
                        print autos



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
    for sdate in getdates:
        #use get_dates to match on snapdaily else return an Autosync
        for snapshot in snapshotlist:
            if re.search(sdate, snapshot):
                print snapshot
                print "hello"
                """
                if re.match("snap-daily", snapshot):
                    print snapshot
                    break
                elif re.match("AutoSync", snapshot) and not re.match("snap-daily", snapshot):
                    print snapshot
                """

def return_snapshots1():
    snapshotlist = get_list_of_snapshots()
    getdates = get_dates()
    for sdate in getdates:
        for snapshot in snapshotlist:
            if re.search(sdate, snapshot) and re.match("snap-daily", snapshot):
                print snapshot



def get_daily_snapshot(thislist):
    new_array = []
    for dsnaps in thislist:
        date = re.split("(\d{4}\-\d{2}\-\d{2})", dsnaps)
        #print date[1]
        if date[1] in  dsnaps:
            if re.match("snap-daily", dsnaps):
                new_array.append(dsnaps)
            elif re.match("AutoSync", dsnaps):
                new_array.append(dsnaps)
                print "this"


print return_snapshots()