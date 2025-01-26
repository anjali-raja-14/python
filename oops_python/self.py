class Dog:

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self.follower=0 # Set default atribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name) 
print(dog1.age)
print(dog1.follower)