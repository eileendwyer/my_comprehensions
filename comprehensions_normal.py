# Remove vowels from the sentence.
my_list = ["List Comprehensions are the Greatest!"]
string_list = ''.join(my_list)
vowels = ['a', 'e', 'i', 'o', 'u']
end = []
for letter in string_list:
    if letter not in vowels:
        end.append(letter)
        "".join(end)

print("".join(end))
#= =========================================
# Remove vowels from the sentence.
my_string = "List Comprehensions are the Greatest!"
vowels = ['a', 'e', 'i', 'o', 'u']

end = [letter for letter in my_string if letter not in vowels]
print(end)
print("".join(end))

#= ========================================
#Create list of water temps for each date
import csv

# each loop iteration over csv.DictReader file produces a dictionary from strings to strings. /
#The keys are the names of the columns (from the first row of the file, which is skipped over), /
# and the values are the data from the row being read.

data_input = csv.DictReader(open("water_data.csv"))
temp = int(row["water temp"])
date = int(row["date"])

print({}, {}.format(temp, date))
#= ================================
#Convert water temp to float
import csv
import math
data_input = csv.DictReader(open("water_data.csv"))
temp = int(row["water temp"])
date = int(row["date"])

end = []
for number in len(temp):
    math.floor(number)
    end.append(number)
print(end)

# for items in len(temp):
#= ====================
# Convert water temp from C to F
import csv
import math
#!/usr/bin/env python
data_input = csv.DictReader(open("water_data.csv"))
Fahrenheit = 9.0/5.0 * Celsius + 32
Celsius = int(row["water temp"])
end = []

for number in len(Celsius):
    return(Fahrenheit)
    end.append(number)
print(end)
#= ================
#Create dictionary with key = Date and value = Wave Height
import csv

data_input = csv.DictReader(open("water_data.csv"))

date = int(row["date"])
wave_height = int(row["wave height"])

for day in date:
print('{} : {}'.format(date, wave_height)

#= ===========================
#Create dictionary w/ average wave height per day
import csv
import math

data_input = csv.DictReader(open("water_data.csv"))

date = int(row["date"])
wave_height = int(row["wave height"])
wave_period = int(row["wave period"])
avg_height = (math.floor(wave_height)/(math.floor(wave_period))

for day in len(date):
print('{} : {}'.format(date, avg_height)

#= ===========================
#Create a nested comprehension to get the average of the Homework 1 grades.
homework_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}
                 }
def average(scores):
    return sum(scores) / len(scores)

sum = sum([homework_dict[r][1]for r in (0, 1, 2)])
    return(sum/len[r1])
    print(average(scores))

average(scores)




