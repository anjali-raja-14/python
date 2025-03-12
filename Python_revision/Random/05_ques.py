import random as r
names=input("Enter the names separated by comma: ")
name=names.split(',')
print(f"{r.choice(name)} will pay the bill")

"""
['Anjali ', ' Ritesh ', ' Yash']
Anjali  will pay the bill
"""
