a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
if(b==0):
    raise ZeroDivisionError("hey our program can't divide by 0 ")
else:
    print(f"The divison of {a}/{b}: {a/b} ")

      