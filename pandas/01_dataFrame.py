import pandas as pd 
# list = ['annna' , 'bihari' , 'chawal' , 'donate']
# res = pd.DataFrame(list)
# print(res)

# people = {'BIhari' : ['chawal'] , 'Anna': ['100 literacy'] , 'Bulla':['allimdulah']}
# category = pd.DataFrame(people , index = ['a','b','c'])
# print(category)


# print(pd.read_csv("F:\\customer (1).csv").head())
# print.head(5)


         # DESCRIBE FUN.

# data = [[34,57,34],[3,43,43] , [34,34,3]]
# print(pd.DataFrame(data))
# print(pd.DataFrame(data).describe())


# dftonumpy = print(pd.DataFrame(data).to_numpy())     # is numpy m cnvery kr dega 



#                  DROP FUNCTION

# data = {'Name' : ['yuvraj' , 'naraayan ' , 'sourabh'],
#     'SEM' : [4,24,12],
#     'Branch' : ['cse ', 'ece' ,'ai']}
# print(pd.DataFrame(data))
# print()
# columns = list(pd.DataFrame(data))
# print(columns)
# print()
# for i in columns:
#     print(i)

#                                                 # Sorting 

#     dsort =pd.DataFrame(data).sort_values(["SEM"], axis = 0 , ascending= [True])
#     print(dsort)



# marks = [45,46,56]
# pd.DataFrame(data)['Marks'] = marks
# print(pd.DataFrame(data))
# print()

# data1 = pd.DataFrame(data).drop(['Name'], axis =1)
# print(data1)
# print()

# print(pd.DataFrame(data).loc[0])       # 1st row ko print kra dega 

# # 
#                                 # new row create knri h
# newRow = pd.DataFrame({'Name' : 'uv' , 'SEM' : 21 , 'Branch': 'power Rangeres'},index =[1])                           
# print(pd.concat([newRow , pd.DataFrame(data) ]).reset_index(drop = True))



#              square in any column


# df = pd.DataFrame({'A':[1,2] , 'B': [10,20]})

# # def square(x):
# #     return x*x
# square  = lambda x:x*x

# print()
# df1 = df.apply(square)
# print(df)
# print(df1)

def change(x) : 
    x["age"] = [10,45,56]
    return x
data = {'Name': ['rgs', 'sef','seg'],
        'age':[35,67,34]}
df = pd.DataFrame(data)
df.pipe(change)
print(df)
