l=[4,3,1,2,0]
len_lst=len(l)
for i in range(len_lst-1):
    for j in range(len_lst-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)


   
        
        


    