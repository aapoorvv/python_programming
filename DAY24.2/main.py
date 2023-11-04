#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name],"
with open("DAY24.2/Input/Names/invited_names.txt","r") as names:
    for name in names.readlines():
        with open(f"DAY24.2/Output/ReadyToSend/{name}.txt","w") as new_letter: 
            with open("DAY24.2/Input/Letters/starting_letter.txt") as letter:
                content = letter.read()
                stripped_name =  name.strip()
                content = content.replace(PLACEHOLDER,stripped_name+",")
            new_letter.writelines(content)