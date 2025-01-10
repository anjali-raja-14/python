a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))
d=int(input("Enter number: "))
if(a>b and a>c and a>d):
    print(f"{a} is greater than {b},{c},{d}")
elif(b>a and b>c and b>d):
    print(f"{b} is greater than {a},{c},{d}")
elif(c>a and c>b and c>d):
    print(f"{c} is greater than {a},{b},{d}")
elif(d>a and d>b and d>c):
    print(f" {d} is grater than {a},{b},{c}")
elif(a==b==c==d):
    print(f"{a}={b}={c}={d}")