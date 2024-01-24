# # FileNotFound

#  try:
#     file = open ("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"{error_message} key does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print(("File was closed."))    
# # raise TypeError

height = float(input("Height in mts: "))
weight = int(input("Weight in kgs: "))
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2 
print(bmi)

