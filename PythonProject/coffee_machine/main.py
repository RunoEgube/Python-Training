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
        print(f"Here is your {user_answer} ☕, Enjoy.")

        resources['water'] = resources['water'] - (MENU["espresso"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["espresso"]['ingredients']['coffee'])
    elif user_answer == 'espresso' and monetary_value == (MENU['espresso']['cost']):
        print(f"Here is your {user_answer} ☕, Enjoy.")
        resources['water'] = resources['water'] - (MENU["espresso"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["espresso"]['ingredients']['coffee'])

    elif user_answer == 'espresso' and monetary_value < (MENU['espresso']['cost']):
        print("Sorry that's not enough money. Money refunded.")


# LATTE
    if user_answer == 'latte' and monetary_value > (MENU['latte']['cost']):
        change = round(float(monetary_value - (MENU['latte']['cost'])), 2)

        Money += (MENU['latte']['cost'])
        print(f"Here is ${change} in change")
        print(f"Here is your {user_answer} 🧋, Enjoy.")

        resources['water'] = resources['water'] - (MENU["latte"]['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - (MENU["latte"]['ingredients']['coffee'])
        resources['milk'] = resources['milk'] - (MENU["latte"]['ingredients']['milk'])
    elif user_answer == 'latte' and monetary_value == (MENU['latte']['cost']):
        print(f"Here is your {user_answer} 🧋, Enjoy.")

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
        print(f"Here is your {user_answer} ☕, Enjoy.")
    elif user_answer == 'cappuccino' and monetary_value == (MENU['cappuccino']['cost']):
        print(f"Here is your {user_answer} ☕, Enjoy.")
    elif user_answer == 'cappuccino' and monetary_value < (MENU['cappuccino']['cost']):
        print("Sorry that's not enough money. Money refunded.")



def espresso_availability():
    if resources['water'] < MENU['espresso']['ingredients']['water']:
        print("Sorry, not enough water")

    elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
        print("Sorry, not enough coffee")
