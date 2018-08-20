import datetime  as dt
curr_datetime = dt.datetime.now()
print("Current year = ", curr_datetime.year)
print("Weekday = ", curr_datetime.weekday())

curr_date = curr_datetime.date()
curr_time = curr_datetime.time()
print("Today's date is = ", curr_date)
print("The time is = ", curr_time)
