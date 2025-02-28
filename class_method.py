# class employee():
#     a=1
#     def show(self):
#         print(f"The class attribute is {self.a}")
# e=employee()
# e.a=45
# e.show()

# o/t:The class attribute is 45


class employee():
    a=1
    @classmethod
    def show(self):
        print(f"The class attribute is {self.a}")
e=employee()
e.a=45
e.show()
