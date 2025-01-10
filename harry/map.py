s = set()
digits = set(map(int, input("Enter numbers separated by spaces: ").split()))
s.update(digits)  # Use `update` to add elements from another iterable or set
print(s)
