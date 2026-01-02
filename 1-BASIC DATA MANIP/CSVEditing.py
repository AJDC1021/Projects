import csv

print("What is the filename?")
filename = input()

dictionary = {}

with open(str(filename), mode = 'r',) as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for line in csvFile:
        dictionary[str(line[0])]=int(line[1])

min_month=0
max_month=0
min=0
max=0
sum=0

for key,value in dictionary.items():
    if min_month == 0:
        min_month = str(key)
        min = int(value)
    else:
        if value < min:
            min_month = str(key)
            min = int(value)

for key,value in dictionary.items():
    if max_month == 0:
        max_month = str(key)
        max = int(value)
    else:
        if value > max:
            max_month = str(key)
            max = int(value)

for key,value in dictionary.items():
    sum += int(value)

average=int(sum/(len(dictionary)))

print("The minimum sales occured in the month of " + min_month + " with a total sale of " + str(min))
print("The maximum sales occured in the month of " + max_month + " with a total sale of " + str(max))
print("The averags sales in the year is " + str(average))








