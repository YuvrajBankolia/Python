# a = input("enter the number: ")
# print("multiplivation table of {a} is : ")
# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {int(a)*i}")
# except Exception as e:
#     print("invalid input ")

# print("SOme imp lines of code")

try:
    num = int(input("enter the numer"))
    a=[3,10 ,45,78,34,59,83,4,49]
    print(a[num])
except ValueError:
    print("number is not a integer ")
except IndexError:
    print("Index Error")
