import csv
from statistics import mean 

with open('auto-mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg = [car for car in mpg if car['horsepower'] != '?']

print(mpg[0].keys())
avgMpg = sum(float(d['mpg']) for d in mpg) / len(mpg)
print('Average miles per gallon: ' + str(avgMpg))

cylinders = set(d['cylinders'] for d in mpg)
cylinders = sorted(cylinders)
mpgPerCylinders = []

for c in cylinders:
    sumMpg = 0
    cylinderTypeCount = 0
    for car in mpg:
        if car['cylinders'] == c:
            sumMpg += float(car['mpg'])
            cylinderTypeCount += 1
    mpgPerCylinders.append((c, (sumMpg / cylinderTypeCount)))

mpgPerCylinders.sort(key=lambda x: x[0])
print(mpgPerCylinders)

horsepowers = set(d['horsepower'] for d in mpg)
horsepowers = [int(x) for x in horsepowers]
horsepowers = sorted(horsepowers)

firstQuater = horsepowers[:len(horsepowers) // 4]
secondQuater = horsepowers[len(horsepowers) // 4:len(horsepowers) // 2]
thirdQuater = horsepowers[len(horsepowers) // 2:len(horsepowers) - len(horsepowers) // 4]
lastQuater = horsepowers[len(horsepowers) - len(horsepowers) // 4:]

groups = []
groups.append(firstQuater)
groups.append(secondQuater)
groups.append(thirdQuater)
groups.append(lastQuater)

mpgPerGroups = []

for group in groups:
    mpgPerGroup = 0
    groupCount = 0
    for car in mpg:
        if int(car['horsepower']) in group:
            mpgPerGroup += float(car['mpg'])
            groupCount += 1
    mpgPerGroups.append((group[-1], (mpgPerGroup / groupCount)))

print(mpgPerGroups)