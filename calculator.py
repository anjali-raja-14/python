def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide  
}
def calculator():
    num1=int(input("Enter the first number: ")) 
    for symbol in operations: 
         print(symbol)

    continue_flag=True
    while  continue_flag:
        op_symbol=input("Pick the operation: ")
        num2=int(input("Enter the second number: "))
        calculator_function=operations[op_symbol]
        output=calculator_function(num1,num2)
        print(f"{num1}{op_symbol}{num2}={output}\n")
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit: \n").lower()
        if(should_continue=='y'):
            num1=output
        elif(should_continue=='n'):
            print("\n************************************************************************\n")
            continue_flag=False
            calculator()
        elif(should_continue=='x'):
            continue_flag=False
            print("Bye")
calculator()   






















