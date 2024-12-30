# a=10
# def sum():
#     c=a+9
#     print(c)
# sum()
# print(a)



a=10
def sum():
    global a
    a=a+9
    print(a)
sum()
