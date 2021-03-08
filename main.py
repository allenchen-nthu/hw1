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
#initialize the number of non available values
no_value = 0
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        no_value = no_value + 1
    elif (target_data[i]["PRES"] == '-999.000'):
        no_value = no_value + 1
    else:
        summation += float(target_data[i]["PRES"])
#put the result into the list
if (no_value == len(target_data)):
    result.append(['C0A880', 'None'])
else:
    #calculating mean
    mean = summation / (len(target_data) - no_value)
    result.append(['C0A880', mean])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0F9A0" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
#initialize the number of non available values
no_value = 0
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        no_value = no_value + 1
    elif (target_data[i]["PRES"] == '-999.000'):
        no_value = no_value + 1
    else:
        summation += float(target_data[i]["PRES"])
#put the result into the list
if (no_value == len(target_data)):
    result.append(['C0F9A0', 'None'])
else:
    #calculating mean
    mean = summation / (len(target_data) - no_value)
    result.append(['C0F9A0', mean])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0R190" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
#initialize the number of non available values
no_value = 0
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        no_value = no_value + 1
    elif (target_data[i]["PRES"] == '-999.000'):
        no_value = no_value + 1
    else:
        summation += float(target_data[i]["PRES"])
#put the result into the list
if (no_value == len(target_data)):
    result.append(['C0R190', 'None'])
else:
    #calculating mean
    mean = summation / (len(target_data) - no_value)
    result.append(['C0R190', mean])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0G640" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
#initialize the number of non available values
no_value = 0
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        no_value = no_value + 1
    elif (target_data[i]["PRES"] == '-999.000'):
        no_value = no_value + 1
    else:
        summation += float(target_data[i]["PRES"])
#put the result into the list
if (no_value == len(target_data)):
    result.append(['C0G640', 'None'])
else:
    #calculating mean
    mean = summation / (len(target_data) - no_value)
    result.append(['C0G640', mean])

# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
#initialize the number of non available values
no_value = 0
#initialize the sum of PRES
summation = 0
#discriminate the value
for i in range(len(target_data)):
    if (target_data[i]["PRES"] == '-99.000'):
        no_value = no_value + 1
    elif (target_data[i]["PRES"] == '-999.000'):
        no_value = no_value + 1
    else:
        summation += float(target_data[i]["PRES"])
#put the result into the list
if (no_value == len(target_data)):
    result.append(['C0X260', 'None'])
else:
    #calculating mean
    mean = summation / (len(target_data) - no_value)
    result.append(['C0X260', mean])
#=======================================

# Part. 4
#=======================================
#sort the staion_id in lexicographical order
result.sort()
# Print result
print(result)
#========================================
