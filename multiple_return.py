def add(a,b):
    if a==0 and b==0:
        return "You have entered zero for both variables\n"
    else:
        return a+b
var1=int(input("Enter the value: "))
var2=int(input("Enter the value: "))
print(f"\n{add(var1,var2)}\n")