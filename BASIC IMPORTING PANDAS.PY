import pandas as pd

# data=[1,2,3,4,5]
# x=pd.Series(data)#default index value are assign for this
# print(x)

# datas=[6,7,8,9,10]
# y=pd.Series(datas,index=['A','B','C','D','E'])#we are assigning index values
# print(y)

# print(y['D'])#accesing the value through index name


# #we can also create a dictoniary while creating a series
# days={"day1":10,"day2":20,"day3":30}
# z=pd.DataFrame(days)
# print(z)

#dataframe
# data={
#     "data":[10,20,30,40,50],
#     "values":[1,2,3,4,5]
# }
# #load data into a df object
# #df=pd.DataFrame(data)
# #print(df)

# #we can name our own index
# df=pd.DataFrame(data,index=['a','b','c','d','e'])
# print(df)

import pandas as pd
#load csv file
df = pd.read_csv('data.csv')
print(df.head())
print(df.tail())
print(df.describe())

# print(df) 