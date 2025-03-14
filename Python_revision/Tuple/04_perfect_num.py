number = int(input("Enter Number: "))  
sum = 0  
for i in range(1, number // 2 + 1): 
    if number % i == 0:  
        sum += i  
if sum == number:  
    print(f"{number} is a perfect number.")  
else:  
    print(f"{number} is not a perfect number.")  
