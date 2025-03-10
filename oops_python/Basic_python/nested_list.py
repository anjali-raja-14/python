
import random
list1=['😎' ,'😎', '😎']
list2=['😎' ,'😎', '😎']
list3=['😎' ,'😎', '😎']#[[1,2,3],[4,5,6][7,8,9]]
matrix=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
position=input("Enter the position in which u want to hide the money: ")
row_num=int(position[0])
column_num=int(position[1])
row_selected=matrix[row_num-1]
row_selected[column_num-1]='x'
print(f"{list1}\n{list2}\n{list3}")








