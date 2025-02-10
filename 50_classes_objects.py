class person:
    name = "uv"
    occupation = "S.D"       # default values inko change bhi kr skte h nich 12 line ke baad
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "yuvraj"
a.occupation = "S.D"
b.name = "try"
b.occupation = "joker"
c.name="bitch"
c.occupation="theif"
a.info()
b.info()
c.info()
