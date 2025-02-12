def greet(fx):
    def mfx(*args , **kwargs):
        print("goof Morning")
        fx(*args ,*kwargs)
        print("thanks for using this function")
    return mfx

       
@greet
def hello():
    print("hello World")
def add(a,b):
    print(a+b)
    
hello()
add(5,2)
#greet(hello)() 