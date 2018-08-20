import datetime as dt
time1 = dt.datetime.now()
time2 = dt.datetime.now()
timediff = time2  - time1
print("Day difference = ", timediff.days)
print("Seconds difference = ", timediff.seconds)
print("Exact seconds difference = ", timediff.total_seconds())
