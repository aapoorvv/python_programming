
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 400,
}
money = 0
def report():
    global money
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")
    
def check_resources(order):
    if resources["water"] >= MENU[order]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                return True
            else:
                return "milk"
        else:
            return "coffee"
    else:
        return "water"
    
def resource_manager(order):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    
def machine(order):
    global money
    if check_resources(order) == True :
        print("\nPlease insert coins:")
        quart = int(input("How many quarters?"))
        dimes = int(input("How many dimes? "))
        nick = int(input("How many nickles? "))
        penny = int(input("How many pennies? "))
        total = (0.01 * penny) + (0.1 * dimes) + (0.05 * nick) + (0.25 * quart)
        if(total >= MENU[order]["cost"] ):
            if(total > MENU[order]["cost"] ):
                change = total - MENU[order]["cost"]
                print(f"\nHere is ${change} in change.")
            print(f"Here is your {order} ☕️. Enjoy!\n")
            money += MENU[order]["cost"]
            return True
        else:
            print(f"\nSorry, that's not enough money. ${total} refunded.\n")
            return False
    else:
        print(f"\nSorry, there is not enough {check_resources(order)}.\n")
        return False
    
while True:
    order = input("What would you like? (espresso/latte/cappuccino: ")
    if order != "report":
        if machine(order):
            resource_manager(order)
    else:
        report()