import csv

# each loop iteration over csv.DictReader file produces a dictionary from strings to strings. /
#The keys are the names of the columns (from the first row of the file, which is skipped over), /
# and the values are the data from the row being read.

data_input = csv.DictReader(open("water_data.csv"))
temp = int(row["water temp"])
date = int(row["date"])

print(list({}, {}.format(temp, date)))

#= ==============================
import math

temp = int(row["water temp"])
end = []
for int in row["water temp"]:
    math.floor(int)
    end.append(int)
print(end)
#= ==========================
#!/usr/bin/env python
Celsius = int(row["water temp"])

