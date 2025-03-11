Year=int(input("Enter year: "))

if(Year%4==0):
    # print("Leap year")
    if(Year%100==0):
        if(Year%400):
            print("It is a leap year")
    else:
       pass
    #    print("leap year")
else:
    print("Not a leap year")