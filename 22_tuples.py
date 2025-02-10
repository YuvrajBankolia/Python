tup = (1,2,45,6,7,87 ,"yuvraj")   #tuple ko change nhi kr skte jo h whi rhe na  kuch usmai add kr skte h 
# tup[0]= 64     aise add nhi kr skte 
print(type(tup) ,tup)
print(tup[0])
print(tup[2])
print(tup[6])
print(tup[3])
print(len(tup))
if 45 in tup:
    print("value is present")
tup = ("hello " , "hi ", "by")
tup2 = ("hhhhh" , "fgfgfgfgfg" , "ergrg")
tup3 = tup+ tup2
print(tup3)