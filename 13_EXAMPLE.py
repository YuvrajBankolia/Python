# import time
# timestamp = time.localtime().tm_hour
# print(timestamp)
# # timestamp = int(time.strftime('good morning'))
# if(timestamp>4 and timestamp<12):
#     print("good morning")
# elif(timestamp>=12 and timestamp<=4):
#     print("good afternoon")
# elif(timestamp>4 and timestamp<9) :
#     print("good evening")
# else: 
#     print("good night")

import time 
t = time.strftime('%H:%M:%S')
timestamp = int(time.strftime('%H'))
print(timestamp)
if(timestamp>0 and timestamp<12):
    print("good morning")
elif(timestamp>=12 and timestamp<=17):
    print("good afternoon")
elif(timestamp>17 and timestamp<=0) :
    print("good evening")
