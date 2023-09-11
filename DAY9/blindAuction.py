from art import logo
import os

def highest(dic):
    bid = 0
    name = ""
    for i in dic:
        if dic[i]>bid:
            bid = dic[i]
            name = i
    return name,bid
        
dic = {}
while(True):
    print(logo)    
    name = input("What is your name?  ")
    bid = int(input("What is your bid?  $"))
    dic[name] = bid
    user = input("Do you want add another bid? yes or no: ")
    if(user=="no"):
        os.system('clear')
        break;
    os.system('clear')
    
name,bid = highest(dic)
os.system('clear')
print(logo)       
print(f"\nThe highest bid is of ${bid} from {name}.\n")
# print(dic)