import random as r
# seed(address)
r.seed(2) #give the same value again and again
for i in range(5):
    print(r.randint(1,100),end="  ")

"""
18  73  98  9  33  
"""


import random

def with_seed():
    random.seed(10)
    print(random.randint(0,100))

def without_seed():
    print(random.randint(0,100))

# without_seed()
with_seed()