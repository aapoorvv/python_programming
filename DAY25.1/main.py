import pandas as pd
# data = []
# with open("DAY25/weather_data.csv","r") as weather_data:
#     for day in weather_data.readlines():
#         data.append(day)
# print (data)

# import csv

# with open("DAY25/weather_data.csv","r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("DAY25.1/weather_data.csv")
print(data)
print('\n')

data_dict = data.to_dict()
print(data_dict)
print('\n')

temp_list = data["temp"].to_list()
print(temp_list)
print('\n')

# print(format(sum(temp_list)/len(temp_list),".1f"))

print("mean: ",data["temp"].mean())
print("median: ",data["temp"].median())
print("mode: ",data["temp"].mode())
print("max: ",data["temp"].max())
print("min: ",data["temp"].min())
print('\n')
# data in columns
print(data.condition)
print('\n')
#data in row
print(data[data.temp == data.temp.max()])
print('\n')

monday = data[data.day == "Monday"]
print(monday)
print (monday.condition)


