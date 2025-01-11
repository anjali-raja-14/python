def reverse(n):
    if(n==0):
        return 0
    return n+reverse(n-1)
n=int(input("Enter the number: "))
print(f"Sum of {n} is {reverse(n)}")


