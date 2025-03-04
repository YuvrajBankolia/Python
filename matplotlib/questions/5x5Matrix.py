import numpy as np
import pandas as pd
import matplotlib as mt


# a =  np.eye(5)             # eye function to make matrix 
# print(a)
# a[a==0] = 4
# print(a)


# a = np.eye(3)
# print(a)
# def dropena(data ):

# data = {'A': [1, 2, None], 'B': [None, 3, 4] , 'B': [6, None, 4] }
# df = pd.DataFrame(data)
# print(df)
# a = df.dropna()
# print(a)

# data = {'A': [1, 2, 3], 'B': [2, 3, 4] , 'C': [6, 9, 4] }
# df = pd.DataFrame(data)
# print(df)
# df = df.rename(columns = {'A':'X' , 'B':'Y' , 'C':'Z'})
# print(df)
# # a = df.dropna()
# print(a)




# data = {'char':['A', 'B' , 'C' , 'A' , 'A']  , 'value' : [10 ,20 ,30 , 45,78]}
# df = pd.DataFrame(data)
# a = df.groupby('char')['value'].sum()
# print(a)



# arr = np.array([0,1,2,2,3,4,4,4,5])
# # a = np.unique(arr)
# # a = np.count_nonzero(arr)
# a =np.bincount(arr)
# print(a)


arr = pd.array([1,3,6,8,9])
a = pd.DataFrame(arr)
print(a)
threshold_value = 6
arr(arr < threshold_value) =10
print(arr)
 
