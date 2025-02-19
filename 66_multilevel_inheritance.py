# # https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0lXZVpHQlAxQldGSGRQdTVsMVFkX3ZRSDg3Z3xBQ3Jtc0tuSElMOU5wczFmYmNiLVNJV2xKdXhHWVRLb0VWTFZSYUtSSW53OVNrd2lxTmVBMnYwX1J4V2pTWFdNdWh3U01TbGhWenlNMTFac2hveU1iVzk5ZlBYa0d3VUl0Q0R5X2FiQVpHQ2pEcjVzUHgtSE1pRQ&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F80-Day-80-Multilevel-Inheritance%23main.py&v=Il7XMJJeXiA


class Animal :
    def __init__(self , name, species):
        self.name = name
        self.species = species
    def show_details(self):
    
        print(f"name:{ self.name}")
        print(f"species:{ self.species}")

class Dog(Animal):
    def __init__(self, name, breed ):
        Animal.__init__(self,name, species="dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
class Rotveiler(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed= "Rotveiler")
        self.color = color
    def show_details(self):
        Dog.show_details()
        print(f" color: {self.color}")

D = Dog("kutta" , "kala")
D.show_details()        


