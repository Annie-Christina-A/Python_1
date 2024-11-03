
Menu={
"latte":{
    "Ingredients":{
        "water":200,
        "milk":150,
        "coffee":24
     },
     "cost":150
    
},
"espresso":{
    "Ingredients":{
        "water":50,
        "coffee":18
     },
     "cost":100
},
"cappuccino":{
        "Ingredients":{
        "water":250,
        "milk":100,
        "coffee":24
     },
     "cost":150
}
}



profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100
}

def input_choice(item):
    for i in item:
        if item[i]>resources[i]:
            print(f"sorry there is not enough {i}")
            return False
    return True
def transaction(amount,price):
        if(amount>=price):
            global profit
            profit+=amount
            balance=amount-price
            print(f"here is your Rs{balance} in change")
            return True
        else:
            print("sorry not sufficient money")
            return False
        
def make_coffee(name,ingridients):
    for i in ingridients:
        resources[i]-=ingridients[i]
    print("enjoy your Coffee ☕")


continue_process=True
while continue_process:
    user=input("what would you like to have? (latte/espresso/cappuccino): ").lower()
    if user=='off':
        continue_process=False
    elif (user=='report'):
        print(f"water={resources['water']}ml")
        print(f"mik={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        user_choice=Menu[user]
        if(input_choice(user_choice["Ingredients"])):
             print("Please insert coins")
             FiveRs=int(input("How may 5Rs. coins: "))
             TenRs=int(input("How may 10Rs. coins: "))
             TwentyRs=int(input("How may 20Rs. coins: "))
             amount=FiveRs*5+TenRs*10+TwentyRs*20
             if(transaction(amount,user_choice["cost"])):
                 make_coffee(user,user_choice['Ingredients'])
   





