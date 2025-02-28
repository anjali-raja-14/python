# n:int= 4
# name:str="Harry"
# def sum(a:int,b:int)->int:# return int
#     return f" Sum:{a+b}"
# print(sum(2,4))


from typing import List, Dict, Tuple, Union

# List of integers
# n: List[int] = [1, 2, 3, 4]
# print(n)

# Tuple containing a string and an integer
t: Tuple[str, int] = ("Hello", 0)
print(t)
# Union contaning a str and int
u:Union[str,int]=("ID1231")
print(u)