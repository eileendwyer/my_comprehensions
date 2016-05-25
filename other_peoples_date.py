import datetime
dates = ["2015 - 08 - 01", .....]

["Monday", "Tuesday", ...]

for date in dates:
    date_list = [int(date_number) fordate_number in date.split("-")

    date_obj = datetime.date(*date_list)
    dow_index = date_obj.weekday()
    #print(date)
    print(days[dow_index]
#= =======================================
###CONVERT THE DATES IN DATA TO STRINGS USING STRFTIME
for date in dates:  ## this is without date_list using strp &Y
    #strfttime.org - get code for year -yr with century as decimal number
    #date_list = [int(date_number) fordate_number in date.split("-")
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()) # from strftime.org Year - month - day
#   date_obj = datetime.date(*date_list)
    #dow_index = date_obj.weekday()
    # print(date)
    print(days[dow_index]

## NOW LIST COMPREHENSION
def get_dow(date_string):
    return([days[datetime.datetime.strptime(date, "%Y-%m-%d").weekday()]]
print[[get_dow(date) for date in dates])


