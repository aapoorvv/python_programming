from art import logo
import os

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

def mod(n1, n2):
  return n1 % n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": mod
}

user = 'n'    
while(True):
    # print(logo)
    if  user =='n':   
        n1 = float(input("What's the first number? "))
    else:
        n1 = ans
        print("First number =",n1)
    op = input("""Pick an operation
+  -  *  /  % ----> """)
    n2 = float(input("What's the next number? "))
    result = operations[op]
    ans = result(n1, n2)
    print(f"\n{n1} {op} {n2} = {ans}\n")
    user = input(f"Type 'y' to continue calculating with {ans} and 'n' to start a new calculation and 'x' to end the program: ")
    os.system('clear')
    if user == 'x':
        break