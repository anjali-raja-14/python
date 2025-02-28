try:
    a=int(input("Enter a number: "))
    print(f"value of a: {a}You are inside try block")
    print("You are inside try block")

except Exception as e:
    print(e)
    print("You are inside exception block")

else:
    print("You are inside else block")