# # https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblNjTGUtMVctRk9vUkU4N1NOOVRTQlZlMXVTQXxBQ3Jtc0trZkU5QnlHTE1WYWNwd01hWkFjbXRkTkVlZHFJaDRlRlpNYlFnTmJERkFGNlpCZ3FrODhYekw5WndQaEZoT0ExbjJ1SU13d09qTEJvdzBWVkVHNTVpQzd1Rl9JWEdtS1Y2dmdGRlRBMnR6dFhhdGtHUQ&q=https%3A%2F%2Freplit.com%2F%40codewithharry%2F71-Day-71-dir-dict-and-help-methods%23main.py&v=Wgo9TaBcuJ4


x = [1,2,34]
# x = (1,2,34)
print(dir(x))
print(x.__add__)

class Person:
    def __init__(self , name , age ):
        self.name = name
        self.age = age
        self.version = 1

p = Person("john " , 45)
print(p.__dict__)


print(help(Person))
        