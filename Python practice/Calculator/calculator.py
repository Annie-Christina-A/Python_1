import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def cal():
    operand1=int(input("Enter first number: "))
    operator={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div,
    }
    for i in operator:
        print(i)
    continue_f=True
    while continue_f:
        pick=input("pick an operator: ")
        operand2=int(input("Enter first number: "))
        chosed=operator[pick]
        cals=chosed(operand1,operand2)
        print(f"{operand1} {pick} {operand2} = {cals}")
        play=input(f"Ener 'y' to continue calculation with {cals} or 'n' to start new calculation or 'x' to exit: ").lower()
        if(play=='y'):
            operand1=cals
        elif(play=='n'):
            continue_f=False
            os.system('cls')
            cal()
        else:
            continue_f=False
cal()







