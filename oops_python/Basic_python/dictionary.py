my_dict = {'nikhil': 1, 'manjeet': 10, 'Amit': 15}
new_dict = {}
for key, value in my_dict.items():
	if key == 'Amit':
		new_dict['Suraj'] = value
	else:
		new_dict[key] = value
del my_dict
my_dict = new_dict
print(my_dict)
