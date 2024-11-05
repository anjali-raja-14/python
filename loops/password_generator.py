# Password_generator
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B' ,'C','D','F', 'G',' H', 'J',' K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z',]
symbol=['@','#','$','%','&','*','(',')']
number=['0','1','2','3','4','5','6','7','8','9']
password_list=[]
print("welcome to password generator!")

n_letters=int(input("How many letter do you want in the password? \n"))
n_symbol=int(input("How many  symbol do you want in the password?\n "))
n_number=int(input("How many number do you want in the password? \n"))

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
   
for i in range(1,n_symbol+1):
    char=random.choice(symbol)
    password_list+=char

for i in range(1,n_number+1):
   char=random.choice(number)
   password_list+=char
print(f"password: {password_list}")
random.shuffle(password_list)
print(f"shuffle password: {password_list}")

password=""
for i in password_list:
    password+=i
print(password)


#    output-
# welcome to password generator!
# How many letter do you want in the password? 
# 2
# How many  symbol do you want in the password?
#  3
# How many number do you want in the password? 
# 4
# password: ['a', 'N', '%', '&', '(', '1', '8', '7', '0']        
# shuffle password: ['(', '0', '8', '7', 'N', '1', '%', '&', 'a']
# (087N1%&a
