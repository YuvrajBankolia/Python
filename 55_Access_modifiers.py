# class employee:
#     def __init__(self):
#         self.__name = "Harry2"   #self.__name isko access nhi kr skte 
# a = employee()
# # print(a.__name)   # cannot be accessed directly
# print(a._employee__name)  # CAn be Accessed indirectly  (a._className__attribute ka name )
# print(a.__dir__())

# next Example

class Student:
    def __init__(self):    
        self._name = "harry"  

    def _funName(self):      # protected Method 
        return "COD"
class Subject(Student):     #inherited class 
    pass

obj = Student()
print(dir(obj))
obj1 = Student()
print(obj._name)
print(obj._funName())


# print(obj1._name)
print(obj1._name)
print(obj1._funName())


