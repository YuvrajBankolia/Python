# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjZOODNnS0JzTC1EQ3hkWnFiYkE1cUNydGJEZ3xBQ3Jtc0tuUkV6N1c2OURfVnRmSTdtS0xFRjBoMDV3dG9FU2ZtWDRaZDNtVkJ5TldleFVGMVFKQTZZNUZrVGFYdGd0bmFsV3czSVdyRE1HREJFQU9QazQyQ0g1Z2JTQUxSTk13UTRTS1Bqb19PRVJROGpFb2ZCNA&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F70-Day-70-Class-methods-as-alternative-constructors%23main.py&v=FGlKJdy--p8

class Employee:
    def __init__(self , name , salary ):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls  ,string):
        return cls(string.split("-")[0] , string.split("-")[1])
e1 = Employee("Yuvraj" , 12000)
print(e1.name)
print(e1.salary)

string ="john-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
