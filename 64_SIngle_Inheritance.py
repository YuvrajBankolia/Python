# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjlxRjhSc2xWMTBwUVJ1UjV0ZWdESDdaTkNWQXxBQ3Jtc0ttLWZLLW9Ic0FGcnhtUWRiM24zaVFTTmdQRUlmUEZxSm03SWk3cVN4VnZwYmdNTVNXSmN2NEcyVU11SVdmZ0RmV1R6UWk0cHg3elM1N2x1bkhxS0ZHX1RmdWlwUUl3a0VlZ01SUTBPekdSN05XekRGdw&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F78-Day-78-Single-Inheritance&v=U53_Gw55NI8
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()