num=input("Enter the no. with space: ")
num_split=num.split()
count=0
for i in num_split:
    count=count+1

for i in range(count):
    num_split[i]=int(num_split[i])

maximum_num=num_split[0]
for number in num_split:
    if  number>maximum_num:
        maximum_num=number
print(f"Maximum number: {maximum_num}")
   
