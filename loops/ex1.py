num=input("Enter the no. with space")
num_split=num.split()
count=0
for i in num_split:
    count=count+1

for i in range(count):
    num_split[i]=int(num_split[i])
print(num_split)

sum=0
for i in num_split:
    sum=sum+i
avg=sum/count
print(round(avg))



