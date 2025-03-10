# def name(f_name,l_name):
#     if f_name==" " and l_name==" ":
#         return "you have entered empty string"
#     else:
#          first=f_name.title()
#          Last=l_name.title()
#          return f"{first} {Last}"
      
# first_name=input("Enter the First Name: ")
# last_name=input("Enter the Last Name: ")
# print(name(first_name,last_name))

def name(f_name, l_name):
    if not f_name.strip() and not l_name.strip():
        return "You have entered empty string"
    else:
        first = f_name.title()
        last = l_name.title()
        return f"{first} {last}"

first_name = input("Enter the First Name: ")
last_name = input("Enter the Last Name: ")
print(name(first_name, last_name))


