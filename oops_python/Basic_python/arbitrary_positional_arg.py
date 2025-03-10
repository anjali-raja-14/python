def fun(*num,name):
    print(num)
    print(name)
fun(1,2,4,5,name="Anjali")

def fun(name,*num):
    print(num)
    print(name)
fun("Anjali",1,2,4,5)

def fun(a,*num):
    print(num)
    print(a)
fun(1,2,4,5)
