# list of mixed datatype 
# list within a list 
list_1=[1,2,3,["Anjali","Raja"],[10,11,["A","B","C"],12,13]]
print(list_1[3]) #['Anjali', 'Raja']
print(list_1[0]) #1
print(list_1[3][0]) #Anjali
print(list_1[4][0]) #10
print(list_1[4][2][1]) #B
print(list_1[4][2][0:]) #['A', 'B', 'C']