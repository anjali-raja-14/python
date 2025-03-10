list_of_dicts = []
n = int(input("Enter the number of queries: "))

for i in range(n):
    name = input("Enter the name: ")
    data = int(input("Enter the data: "))
    dict1 = {name: data}
    list_of_dicts.append(dict1)

sorted_list = sorted(list_of_dicts,value=lambda dict1: list(dict1.value())[0])
print(sorted_list)


