# list comprehension

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# names = ["Alex","Beth", "Caroline","Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len (name) < 5]
# long_names = [name. upper() for name in names if len (name) > 5]
# print(short_names)
# print(long_names)


nums = [1,1,2,3,5,8,13,21,34,55]
# squared_nums = [n*n for n in nums]
# print(squared_nums)

# even_nums = [n for n in nums if n%2==0]
# print(even_nums)

with open("DAY26/file1.txt") as file1:
    c1 = file1.readlines()
with open("DAY26/file2.txt") as file2:
    c2 = file2.readlines()
c = [int(n1) for n1 in c1 if n1 in c2]
print(c)
    
        
