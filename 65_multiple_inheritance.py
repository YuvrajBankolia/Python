
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUNlVlZFejI3NFZVcjEwZGRpaG9lNWVNSVpaQXxBQ3Jtc0ttUUV4NXBYYk1tb0JoSE90cDZ5NWdYYmxwY2Z0Q2gzekJvUTlPQVBQODJCQktDZlpQSTNFWjN4VE11RS1ENXZVQlkyRkFVZmJEV0o4aGM1UC1paFljdXF5bENod01aVXBLOElQaVYzazhpMHRDYXFjOA&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F79-Day-79-Multiple-Inheritance&v=4o7xSHgKlvI

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())