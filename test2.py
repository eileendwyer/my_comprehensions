# list of water temp by day
import csv
data_reader = csv.writer(open(water_data_set.csv, 'w', newline='',
                       delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL))
data_reader.writerow