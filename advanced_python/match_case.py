def hey(status=0,name="Anjali"):
    match status:
        case 200:
            print("HEY",name)
        case 300:
            print("HELLO",name)
        case 400:
            print("GOOD LUCK",name)
        case _:
            print("By",name)

hey(200,"Ritesh")
hey(300)
hey(400)
hey()