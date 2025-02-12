class employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the Employee :{self.id} is {self.name}")
class PRogrammer(employee):
    def showLanguage(self):
        print("the default language is Python ")
e1 = employee("YUvraj" , 200)
e1.showDetails()
e2 = PRogrammer("uuuuuuu" , 1)
e2.showLanguage()
e1 = employee("uv" , 2000)
e1.showDetails()
