
# def cube(x):
#     return x*x*x

# print(cube(2))
# l = [2,6,3,7,5]
# newl = list(map(cube,l)) #( func ka name , jisko krna h) function ko function as argument le leta h usk oBOLTE h HIGHER ORDER FUNCTION
# print(newl)

# #   FILTER         ye filter kr dega mtlb 4 se bdi ko print krega
# def filter_function(a):
#     return a>4

# newnewl = list(filter(filter_function , l))  # filter_function hrr value ke liye true ya flase return krega 
#                                             # kyoki jo true hoga wo list m aa jyega
# print(newnewl)



from functools import reduce

number = [ 1,4,3,7,5]
# number = [ 5,3,7,5]
# number = [ 8,7,5]
# number = [ 15,5]
# number = [ 20]                # OUTPUT =20

def mysum(s,y):
    return s+y
sum= reduce(mysum , number)
print(sum)