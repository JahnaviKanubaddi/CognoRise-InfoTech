import os
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def modulo(x,y):
    return x%y
operation_dict={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": modulo
}

def calculator():
    num1=float(input("Enter first number: "))
    for symbol in operation_dict:
        print(symbol)

    countiune_flag=True
    while countiune_flag:
        ope_symbol=input("Pick an operation: ")
        num2=float(input("Enter secound number: "))
        cal_func=operation_dict[ope_symbol]
        output=cal_func(num1,num2)
        print(f"{num1} {ope_symbol} {num2} = {output}")

        should_countinue=input("Enter 'c' to continue calculation with {output}'n' to start a new calculation or 'x' to exit : ").lower()
        if should_countinue == 'c':
            num1 = output
        elif should_countinue == 'n':
             countiune_flag=False
             os.system('cls')
             calculator()

        else:
            countiune_flag=False
            print("Thank You")
calculator()
            
