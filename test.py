import datetime
from collections import defaultdict
import csv


reader = csv.DictReader(open("water_data.csv"))
for row in reader:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    wave_height = (row['Date'], row['Wave Height'])
    dates = row['Date']

    for date in dates:
        date_list = (int(date_number) for date_number in dates.split("/"))
        date_obj = datetime.date(*date_list)
        dow_index = date_obj.weekday()
        #print(dow_index)
        print(days[dow_index])







