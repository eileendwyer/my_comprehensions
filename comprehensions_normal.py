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

# no_vowels = [letter for letter in my_string if letter not in vowels]

#= ========================================
import csv

reader = csv.DictReader(open('water_data.csv'))
for row in reader:
    Celsius_temp = [(row["Water Temp"])]
    print(" Date: ", row['Date'], "Water Temp:", row['Water Temp'])

#= ================================
#Convert water temp to float
import csv
reader = csv.DictReader(open("water_data.csv"))
for row in reader:
    temp = (row["Water Temp"])
    float(temp)
    temp_f = ["Water Temp:", float(temp)]
#    print("Water Temp:", float(temp))
#    print(temp_f)

#= ====================
# Convert water temp from C to F
import csv
reader = csv.DictReader(open("water_data.csv"))
for row in reader:
    Celsius_temp = [(row["Water Temp"])]
    for item in Celsius_temp:
        temp_Fahrenheit = [int(item * 1.8 + 32)]
        print(temp_Fahrenheit)
#= ================
#Create dictionary with key = Date and value = Wave Height
import csv
reader = csv.DictReader(open("water_data.csv"))
wave_height = (" Date: ", row['Date'], "Wave Height:", row['Wave Height'])
#print(" Date: ", row['Date'], "Wave Height:", row['Wave Height'])


#= ===========================
#Create dictionary w/ average wave height per day
import csv
import math


#= ===========================
#Create a nested comprehension to get the average of the Homework 1 grades.
homework_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}
                 }
def average(scores):
    return sum(scores) / len(scores)

#sum = sum([homework_dict[r][1]for r in (0, 1, 2)])
#return(sum/len[r1])
#print(average(scores))

average(scores)

#= ================




