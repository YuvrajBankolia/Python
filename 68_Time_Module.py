import time

# def usefor():
#     for i in range(500):
#         print(i)
# def useWhile():
#     i=0
#     while i<500:
#         i=i+1
#         print(i)
# init = time.time()
# usefor()
# print(time.time()-init)
# init = time.time()
# useWhile()
# print(time.time()-init)

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 