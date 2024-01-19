student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:

# for(key, value) in student_dict.items() :
#     print(value)
#     print(key)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print (student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index,row) in student_data_frame.iterrows():
    print(row)
    print(index)
