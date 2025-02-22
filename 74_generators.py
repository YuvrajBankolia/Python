def my_generator():
    for i in range(5):
        yield i     # mauke pr generate krta h values ko jb jrurt hoti h tb 
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen)) 

for j in gen:
    print(j)