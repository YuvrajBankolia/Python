# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbm9tZlhRa21PeTBUNmF5R0c0LUxaeEZfWTcwQXxBQ3Jtc0trelZPVDRSVEhYRHhCWC0xM1J4dVNNdEViU3FMM1h2M3pNWlV2ZVBlLWFYdGlpLUFaVGc2Q0RCelA2NTVQN2JzZjBuQUFkOFZoVm83MGlnaFlnWm93NnBmd2NUUmpFZDhabU8weU9LVElhSVZtUlpKNA&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F72-Day-72-super-Keyword%23main.py&v=P648reefNh0

class baseClass:
    def base_method(self):
        print("this is the parent method")
class derivedClass(baseClass):
    # def base_method(self):
    #     print("Harry")
    #     super().base_method()

    def derived_method(derivedClass):
        print(" this is the derived class")

        super().base_method()
child_object = baseClass()
child_object.base_method()
child_object = derivedClass()
child_object.derived_method()
child_object.derived_method()


class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id , lang):
        super().__init__(name, id )
        self.lang = lang
rohan = Employee("Rohan das" ,"3434")
harry= Programmer("hArry das" , "6776" , "python")

print(harry.name)
print(harry.id)
print(harry.lang)
print(rohan.name)