# :=walrus operator
if( n:=len([2,4]))>3:
    print(f"The list is too long ({n} element expected <=3)")
else:
    print(f"The list is short ({n} element expected >=3)")