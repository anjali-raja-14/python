# char_c=input("Enter the character: ")
# def check_vowel():
#     vowel="a","e","i","o","u"
#     match char_c:
#         case "a" | "e" | "i" | "o" | "u" | "A" | "E "| "I" | "O" | "U":
#             print("Character is vowel")
#         case _:
#             print("Character is a consonent")
# char_length=len(char_c)
# if(len(char_c)>1):
#     print("Pls.......\nEnter only one character")
# else:
#     check_vowel()

# import math

# list=[0,4,3,7,0]
# len_list=len(list)
# n=(len_list/2) #2.5
# x=math.ceil(n) #3
# for i in range(x):
#     if(i!=x and list[i]==list[len_list-1] ):
       
#         print('series is palindrome')
#         break
# else:
#     print('series is not palindrome')

import math
list = [0, 4, 3, 4, 0]
len_list = len(list)
n = len_list / 2
x = math.ceil(n)
for i in range(x):
    if list[i] != list[len_list - i - 1]: 
        print('Series is not palindrome')
        break
else:
    print('Series is palindrome')







