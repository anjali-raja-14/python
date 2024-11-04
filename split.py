import random
a=input("Enter the name separated by comma: ")
text_split=a.split(",")
print(text_split)
length=len(text_split)
print(length)
random=random.randint(0,length-1)
print(f"{text_split[random]} will pay the bill")

print(random.choice(text_split))
