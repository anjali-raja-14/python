dict1={
    "name":"Anjali",
     "subjects":
     {
         "Maths":83,
         "English":23,
         "science":44
     }
}

print(dict1["name"])
#Anjali

print(dict1["subjects"]["Maths"])
#83

print(list(dict1.keys()))
#['name', 'subjects']

print(list(dict1.values()))
#['Anjali', {'Maths': 83, 'English': 23, 'science': 44}]

print(len(dict1.values()))
# 2

print(dict1.items())
# dict_items([('name', 'Anjali'), ('subjects', {'Maths': 83, 'English': 23, 'science': 44})])

print(dict1.get("name"))
#Anjali

new_dict={
    "name":"Ritesh"
}
dict1.update(new_dict)
print(dict1)
# {'name': 'Ritesh', 'subjects': {'Maths': 83, 'English': 23, 'science': 44}}

