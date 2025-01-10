# s=set()
# s.add("18")
# s.add(18)
# print(s)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))
# 20 == 20.0  # True


# output:
# {'20', 20}
# 2


a= [1, 2, 3]
b = [1, 2, 3]
print(a==b)#true
print(a is b)#true