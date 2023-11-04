with open("DAY24.1/myfile.txt") as file:
    contents = file.read()
    print(contents)
    
with open("DAY24.1/myfile.txt", mode="a") as file:
    file.write("\nnew text.")
    
with open("new_file", mode="w") as newfile:
    file.write("\nnew text.")  