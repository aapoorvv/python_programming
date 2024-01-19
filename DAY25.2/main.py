import pandas as pd

squirrel_data = pd.read_csv("DAY25.2/Squirrel_data.csv")
dict = (squirrel_data["Primary Fur Color"].value_counts())
print(dict)
dict.to_csv("DAY25.2/Squirrel_count.csv")

