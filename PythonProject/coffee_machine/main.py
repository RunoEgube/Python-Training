MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = 0

def collect_payment():
    global Money
    quarter = int(input("Please insert coins.\nHow many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    quarter = float(quarter * 0.25)
    dime = float(dime * 0.10)
    nickel = float(nickel * 0.05)
    penny = float(penny * 0.01)
    monetary_value = quarter + dime + nickel + penny
# ESPRESSO
    if user_answer == 'espresso' and monetary_value > (MENU['espresso']['cost']):
        change = round(float(monetary_value - (MENU['espresso']['cost'])), 2)

        Money += (MENU['espresso']['cost'])
        print(f"Here is ${change} in change")
        print(f"Here is {user_answer}, Enjoy.")

        resources['water'] = resources['water'] - (MENU["espresso"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["espresso"]['ingredients']['coffee'])
    elif user_answer == 'espresso' and monetary_value == (MENU['espresso']['cost']):
        print(f"Here is {user_answer}, Enjoy.")
        resources['water'] = resources['water'] - (MENU["espresso"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["espresso"]['ingredients']['coffee'])

    elif user_answer == 'espresso' and monetary_value < (MENU['espresso']['cost']):
        print("Sorry that's not enough money. Money refunded.")


# LATTE
    if user_answer == 'latte' and monetary_value > (MENU['latte']['cost']):
        change = round(float(monetary_value - (MENU['latte']['cost'])), 2)

        Money += (MENU['latte']['cost'])
        print(f"Here is ${change} in change")
        print(f"Here is {user_answer}, Enjoy.")

        resources['water'] = resources['water'] - (MENU["latte"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["latte"]['ingredients']['coffee'])
        resources['milk'] = resources['milk'] - (MENU["latte"]['ingredients']['milk'])
    elif user_answer == 'latte' and monetary_value == (MENU['latte']['cost']):
        print(f"Here is {user_answer}, Enjoy.")

        resources['water'] = resources['water'] - (MENU["latte"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["latte"]['ingredients']['coffee'])
        resources['milk'] = resources['milk'] - (MENU["latte"]['ingredients']['milk'])
    elif user_answer == 'latte' and monetary_value < (MENU['latte']['cost']):
        print("Sorry that's not enough money. Money refunded.")


#CAPPUCCINO
    if user_answer == 'cappuccino' and monetary_value > (MENU['cappuccino']['cost']):
        change = round(float(monetary_value - (MENU['cappuccino']['cost'])), 2)

        Money += (MENU['cappuccino']['cost'])
        print(f"Here is ${change} in change")
        print(f"Here is {user_answer}, Enjoy.")
    elif user_answer == 'cappuccino' and monetary_value == (MENU['cappuccino']['cost']):
        print(f"Here is {user_answer}, Enjoy.")
    elif user_answer == 'cappuccino' and monetary_value < (MENU['cappuccino']['cost']):
        print("Sorry that's not enough money. Money refunded.")



def espresso_availability():
    if resources['water'] < MENU['espresso']['ingredients']['water']:
        print("Sorry, not enough water")

    elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
        print("Sorry, not enough coffee")

    else:
        collect_payment()

def cappuccino_availability():
    if resources['water'] < MENU['Cappuccino']['ingredients']['water']:
        print("Sorry, not enough water")

    elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
        print("Sorry, not enough coffee")

    elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
        print("Sorry, not enough milk")
    else:
        collect_payment()

def latte_availability():
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry, not enough water")

        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry, not enough coffee")

        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry, not enough milk")
        else:
            collect_payment()

# TODO 2: PRINT A REPORT OF THE COFFEE'S RESOURCES
# TODO 1: prompt user to enter answer
should_continue = True
while should_continue:
    user_answer = input("What would you like? (espresso/latte/Cappuccino):").lower()
    if user_answer == 'report':
        report = f"water:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:{Money}"
        print(report)
    elif user_answer == 'espresso':
        espresso_availability()

    elif user_answer == 'latte':
        latte_availability()

    elif user_answer == 'cappuccino':
        cappuccino_availability()

    elif user_answer == 'off':
        should_continue = False


# TODO 3: turn off the machine by entering off
# TODO 4: check resources sufficient
# TODO 5: Process coins
# TODO 6: check transaction successful
# TODO 7: Make coffee


