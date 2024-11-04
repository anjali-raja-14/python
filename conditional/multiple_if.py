height=float(input("Enter your height(feet): "))
print(f"your height is {height} ")
if(height>=3):
    print("You can ride")
    age=int(input("Enter your age: "))
    if(age>=18):
        print("Ticket price is  500 ")
        bill=500
    if(age<18):
        print("Ticket price is  250  ")
        bill=250
    photo=input("Do you want to take photo?: ")
    if(photo=="yes"):
        bill=bill+50
        print(f"You have to pay {bill}")
else:
    print("You can't ride")
print("Bye")