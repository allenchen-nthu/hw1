# hw1
# (1) How to setup and run the program
#     1. Visit https://gitlab.larc-nthu.net/ee2405_2021/hw1/.
#     2. Download "108061105.csv".
#     3. Clone the code and then execute.
# (2) The following is the output result. (['station_id', mean of PRES])
# [['C0A880', 1016.9416666666666], ['C0F9A0', 967.5478260869564], ['C0G640', 1017.2166666666666], ['C0R190', 1011.2583333333332], ['C0X260', 1012.1625]]
# (3) Design method:
#     1. Part. 1
#        Import csv module.
#     2. Part. 2
#        Read cwb weather data.
#        Put the csv data into the list.
#        *If you are interested in processing other csv file, change '108061105.csv' into your csv file name. (line 11)
#     3. Part. 3
#        Create a list to store the results.
#        Retrive all data points of the designated station into the target data list.
#        Remove the PRES data if the value is '-99.000' or '-999.000'
#        Calculate the mean (or 'None' if the average can't be calculated) and append it to the result list.
#     4. Part. 4
#        Sort the station_id in lexicographical order.
#        Output the result.
#
# *other details of how the code works are in the comment of main.py
