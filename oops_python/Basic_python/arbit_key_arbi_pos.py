def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key ,value)
    print(args)
info_person(1,2,3,Name="Ritesh Suryavanshi ",Department="CS ",Age=30)
info_person(1,2,3,Name="Anjali Raja ",Department="DS ",Age=20)
        