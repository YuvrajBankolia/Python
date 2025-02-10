# def double(x):
#     return x*2



def appl(fx , value):
    return 6+ fx(value)   # ismai function ke andr function ka use kr rha h toh isko lambda ka use krkrke ek lime m bhi kr skte h 



double = lambda x:x*2   # lambda ko use krne ke baad upper wale code ko 1 line m kr dega 
                        # complexity lm krega chota code 
cube = lambda x: x*x*x
avg = lambda x,y,z : (x+y+z)/3
print(double(5))
print(cube(5))
print(avg(5 ,6, 3))
print(appl(lambda x: x*x*x , 5))