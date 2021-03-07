# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061105.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================
# Part. 3
#=======================================
result = []
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0A880" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
#initialize status of full available values
status = 1
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        status = 0
    elif (target_data[i]["PRES"] == '-999.000'):
        status = 0
    else:
        summation += float(target_data[i]["PRES"])
#calculating mean
mean = summation / len(target_data)
#put the result into the list
if (status == 1):
    result.append(['C0A880', mean])
else:
    result.append(['C0A880', None])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0F9A0" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
#initialize status of full available values
status = 1
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        status = 0
    elif (target_data[i]["PRES"] == '-999.000'):
        status = 0
    else:
        summation += float(target_data[i]["PRES"])
#calculating mean
mean = summation / len(target_data)
#put the result into the list
if (status == 1):
    result.append(['C0F9A0', mean])
else:
    result.append(['C0F9A0', None])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0R190" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
#initialize status of full available values
status = 1
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        status = 0
    elif (target_data[i]["PRES"] == '-999.000'):
        status = 0
    else:
        summation += float(target_data[i]["PRES"])
#calculating mean
mean = summation / len(target_data)
#put the result into the list
if (status == 1):
    result.append(['C0R190', mean])
else:
    result.append(['C0R190', None])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0G640" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
#initialize status of full available values
status = 1
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        status = 0
    elif (target_data[i]["PRES"] == '-999.000'):
        status = 0
    else:
        summation += float(target_data[i]["PRES"])
#calculating mean
mean = summation / len(target_data)
#put the result into the list
if (status == 1):
    result.append(['C0G640', mean])
else:
    result.append(['C0G640', None])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
#initialize status of full available values
status = 1
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        status = 0
    elif (target_data[i]["PRES"] == '-999.000'):
        status = 0
    else:
        summation += float(target_data[i]["PRES"])
#calculating mean
mean = summation / len(target_data)
#put the result into the list
if (status == 1):
    result.append(['C0X260', mean])
else:
    result.append(['C0X260', None])
#=======================================

# Part. 4
#=======================================
#sort the staion_id in lexicographical order
result.sort()
# Print result
print(result)
#========================================
