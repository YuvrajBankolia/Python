x=10
def fun():
    global x
    x =20
    y=5
    print("the value of local variable is " ,y)

fun()
print("the value of global variable is" ,x)
# print(y)    ye run nhi hoga kyo ki y ek local variable aur yaha prr globally access krna chahta h 