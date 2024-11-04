print("1.Small pizza")
print("2.Medium  size pizza")
print("3.Large size pizza")
choice=int(input("Enter your choice?: "))
if(choice==1):
    amount=100
    print("Pay 100 Rupees")
if(choice==2):
    amount=200
    print("Pay 200 Rupees")
if(choice==3):
    amount=300
    print("Pay 300 Rupees")
choice1=input("Do you want pipperoni: ")
if(choice1=="yes"):
    if(choice==1):
        print(f"Total amount: {amount+20}")
    if(choice==2):
        print(f"Total amount: {amount+40}")
    if(choice==3):
        print(f"Total amount: {amount+60}")
else:
    print("bye")






