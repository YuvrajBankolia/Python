# # # # a = True 
# # # print(a := False)

# # numbers = [1,2,3,4,5]

# # while(n:=len(numbers))>0:
# #     print(numbers.pop())

# happy = False
# print(happy)

# print(happy:=True)



# WITHOUT USING THE WALRULS OPERATOR
# foods= list()
# while True :
#     food = input("What food do you like?: ")
#     if food =="quit":
#         break
#     foods.append(food)


# WIT USING THE WALRULS OPERATOR
foods = list()
while (food := input("what the food do you like? : "))!="quit":
    foods.append(food)