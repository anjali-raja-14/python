height=int(input("Enter your height(feet): "))
print(f"your height is {height} ")
if(height>=3):
    print("You can ride")
    age=int(input("Enter your age: "))
    if(age>=18):
        print("You have to give 250 rupees")
    elif(age<18):
        print("you have to give 150 ruppes ")
else:
    print("You can't ride")
print("Bye")