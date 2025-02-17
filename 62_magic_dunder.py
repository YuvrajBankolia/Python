class Employee:
    # name = " Harry"
    def __init__(self , name): # constructor
        self.name = name
        
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
e= Employee("Harry")


def __repr__(self):
    print(f"employee('{self.name})")
def __call__(self):
    print(" Hey i am good")
#print(e.name)
#print(len(e))   # bina __len__ ko call kre length print krwa dii