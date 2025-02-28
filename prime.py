# prime or not
n=int(input("Enter a number: "))
for i in range(2,n):
    count=0
    if(n%i==0):
        print("The number is not prime")
        break
else:
    print("The number is prime")
      
   