# # phone_no={
# #     'Anjali':[1234,1234,4433],
# #     'Yash':678910,
# #     'Khushi':23456
# # }
# # print(phone_no)




# dict = {}
# n = int(input())
# for i in range(n):
#     key = input()
#     v1 = int(input())
#     v2 = int(input())
#     v3 = int(input())
#     dict[key] = v1,v2,v3
# query=input()
# dict2=dict[query]
# dict2=(v1+v2+v3/3)
# print(dict2)




dict = {}
n = int(input())
for i in range(n):
    key, v1, v2, v3 = input().split()
    dict[key] = (float(v1), float(v2), float(v3))
query = input()
if query in dict:
    v1, v2, v3 = dict[query]
    average = (v1 + v2 + v3) / 3
    avg=round(average,2)
    print(avg)
else:
    print("Name not found")
