text=input("Enter any text by giving space: ")
list1=[]
list2=[]
list1=text.split(" ")
print(list1)
list2=list1.copy()
list2.reverse()
print(list2)
print("Palindrome list") if(list1==list2) else print("Not Palindrome list")

