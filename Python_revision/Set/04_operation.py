set1={"Anjali","Yash","Falaq","Bhaiyu","Ritesh"}
set2={"Anjali","Himanshu","Jyoti"}
set3={"Ritesh"}
print(set1.difference(set2))#set1-set2(item 1 but not in set2)
# {'Ritesh', 'Falaq', 'Yash', 'Bhaiyu'}
print(set1.symmetric_difference(set2))#common ko chod kr sabhi value aaygi
# not allowed in multiple set
print(set1^set2)
# {'Jyoti', 'Yash', 'Falaq', 'Ritesh', 'Bhaiyu', 'Himanshu'}
# {'Jyoti', 'Himanshu', 'Yash', 'Ritesh', 'Bhaiyu', 'Falaq'}
print(set1^set2^set3)
# {'Falaq', 'Yash', 'Bhaiyu', 'Jyoti', 'Himanshu'}