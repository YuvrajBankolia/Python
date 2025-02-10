class person:
    # name = "harry"
    # occ = "Developer"

    def __init__(self):       # DEFAULT CONSTRUCTOR
        print("hey i am a prsn")
    def __init__(self ,name , occ):       # PARAMERIZED CONSTRUCTOR
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("harry" , "developer")
b = person("hhhhhhh" ,'iiiiiii')
# a.name = "hii"
# a.occ = "gesg"
# #print#(a.info)#
a.info()   
b.info()
