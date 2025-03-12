list1=["🥰","🥰","🥰"]
list2=["🥰","🥰","🥰"]
list3=["🥰","🥰","🥰"]
list4=[list1,list2,list3]
print( list1,"\n",list2,"\n",list3)
Row=int(input("Enter the position of row: "))
Column=int(input("Enter the position of column: "))
list4[Row-1][Column-1]="😡"
print( list1,"\n",list2,"\n",list3)
