class employee:
    def __init__(self):
        self.__name = "Harry"   #self.__name isko access nhi kr skte 
a = employee()
# print(a.__name)   # cannot be accessed directly
print(a._employee__name)  # CAn be Accessed indirectly