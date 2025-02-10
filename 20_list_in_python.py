marks = [3,5,7,"harry" , True ,5, 8, 9]
print((type(marks)))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-3])   # negative index
print(marks[len(marks)-3])   # positive index
print(marks[5-3])
print(marks[2])

if 7 in marks:
    print("yes")
else:print("no")


print(marks)
print(marks[1:8])
print(marks[1:8:3])  # jump by 3 


lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)