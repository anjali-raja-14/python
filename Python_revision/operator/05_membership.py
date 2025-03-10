a="Anjali Raja"
print("A" in a)
print("N" not in a)


# Python program to illustrate the use
# of 'is' and '==' operators
a = [1, 2, 3]
b = [1, 2, 3]
# using 'is' and '==' operators
print(id(a))
print(id(b))
print(a is b)
print(a == b)


x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Equality comparison (==)
if x == y:
    print("True")
else:
    print("False")



