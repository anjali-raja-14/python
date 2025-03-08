# too complexity
# import math
# a=int(input("Enter any number: "))
# b=a/2
# math.floor(b)
# b=int(b)
# for i in range(b):
#     a=a-2
#     i=i+1
# if(a==1):
#     print("The number is odd")
# else:
#     print("The number is even")


a = int(input("Enter any number: "))

if a & 1:  # Checks if the least significant bit is 1 (odd)
    print("The number is odd")
else:
    print("The number is even")
