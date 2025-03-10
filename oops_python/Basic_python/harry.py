# n=int(input("Enter the number:  "))
# for i in range(11):
#     print(i*n)


# l= ["Anjali","Ritesh","Raja"]
# for i in l:
#     if(i.startswith("R")):
#         print("Hii", i)


# prime or not
# n=int(input("Enter a number: "))
# for i in range(2,int(n/2)):
#     count=0
#     if(n%i==0):
#         print("The number is not prime")
#         break
# else:
#     print("The number is prime")


# find the sum of first 10 natural number
# a=int(input("Enter the number: "))
# i=1
# sum=0
# while(i<=a):
#     sum+=i
#     i=i+1
# print(f"Sum of first {a} natural number is {sum}")


# factorial
# a=int(input("Enter the number: "))
# i=1
# factorial=1
# while(i<=a):
#     factorial*=i
#     i=i+1
# print(f"Factorial of first {a}  number is {factorial}")
      

# n=int(input("Enter the number:  "))
# for i in range(1,11):
#     print(n*(11-i))
# 1 + 10=11
# 2 + 9=11
# 3 + 8=11
# 4 + 7=11
# 5 + 6=11
# 6 + 5=11



# factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter the number: "))
print(f"The factorial of {n}: {factorial(n)}")