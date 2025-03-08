num = int(input("Enter any number: "))
check_even = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even(num))