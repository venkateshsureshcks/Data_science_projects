Menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
            "ingredients":{
                "water": 200,
                "milk":150,
                "coffee":24,

            },
            "cost":2.5,
        },
    "cappuccino":{
            "ingredients":{
                "water": 250,
                "milk":100,
                "coffee":24,
            },
            "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0

def Is_resource_sufficient( order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough of {item}")
            return False
    return True

def Process_coins():
    total = int(input("Insert a coins :"))
    return total

def Is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ur change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry there is no enough money")
        return False

def Make_coffee(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on :
    choice = input("What Would you like ? (espresso/ latte/ cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}ml")
        print(f"profit : ${profit}")
    else:
        drink = Menu[choice]
        if Is_resource_sufficient(drink["ingredients"]):
            payment = Process_coins()
            if Is_transaction_successful(payment, drink["cost"]):
                Make_coffee(choice, drink["ingredients"])




