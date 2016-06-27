# Remove vowels from the sentence.
my_string = "List Comprehensions are the Greatest!"
"".join(my_string)
vowels = ['a', 'e', 'i', 'o', 'u']
no_vowels = []
for letter in my_string:
    if letter not in vowels:
        no_vowels.append(letter)
        "".join(no_vowels)
        print("".join(no_vowels))

no_vowels = [letter for letter in my_string if letter not in vowels]

#= ========================================
#Create list of date and water temp
import csv

reader = csv.DictReader(open('water_data.csv'))
for row in reader:
    Celsius_temp = [(row["Water Temp"])]
    print(" Date: ", row['Date'], "Water Temp:", row['Water Temp'])

#= ================================
#Convert water temp to float
import csv
reader = csv.DictReader(open("water_data.csv"))
temp = [float(temp) for(row["Water Temp"]) in reader]
#for row in reader:
#    temp = (row["Water Temp"])
#    float(temp)
print("Water Temp:", float(temp))
#    print(temp_f)

#= ====================
# Convert water temp from C to F
import csv
reader = csv.DictReader(open("water_data.csv"))
#for row in reader:
#    Celsius_temp = [(row["Water Temp"])]
#    for item in Celsius_temp:
temp_F = [[int(item * 1.8 + 32)] for (row["Water Temp"]) in reader]
print(temp_F)
#= ================
#Create dictionary with key = Date and value = Wave Height
import csv
reader = csv.DictReader(open("water_data.csv"))
for row in reader:
    wave_height = (row['Date'], row['Wave Height'])
    print(wave_height)


#= ===========================
#Create dictionary w/ average wave height per day-of-week
import datetime
from collections import defaultdict

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_dow(date_string):
    print(day[datetime.datetime.strptime(date_string, "%Y-%m-%d").weekday()])

get_dow()
def wave_summary():
    new_list = [(get_dow(day), float(wave)) for day, wave in timeline.items()]
    # print(new_list)

    waves_by_day = defaultdict(list)
    for day, wave in new_list:
        waves_by_day[day].append(wave)
    # print(waves_by_day)

    avg_waves_by_day = {}
    for day, wave in waves_by_day.items():
        avg_waves_by_day[day] = sum(wave) / len(wave)
    # print(avg_waves_by_day)
wave_summary()


#= ===========================
#Create a nested comprehension to get the average of the Homework 1 grades.
from collections import defaultdict
from statistics import mean


def homework_avg():

    scores = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}
                 }

    #    for name in scores:
    #    avg = mean(scores([name]['Homework 1'])
#    print(mean([scores[name]['Homework 1'] for name in scores]))
    return mean([scores[name]['Homework 1'] for name in scores])

homework_avg()





