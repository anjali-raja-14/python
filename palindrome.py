my_list = []
num_elements = int(input("How many elements do you want in the list? "))

for i in range(num_elements):
    user_input = input("Please enter element {}: ".format(i+1))
    my_list.append(user_input)

print("Your list is:", my_list)
copy_list=my_list.copy()
print(my_list)

my_list.reverse()
print(my_list)

if(copy_list==my_list):
    
    print("The list is palindrome ")
else:
    print("The list is not palindrome")

