# 1.lambda function--a lambda fuctio is a small anonymous function defied using the lambda keyword
# lambda--function create chestundhi
# x--iput parameter
# x+5--calculation
# add_five=lambda x:x+5
# print(add_five(10))

# apply()--the apply( method applies a function along a pandas series or dataframe axis)
import pandas as pd
df=pd.DataFrame({
    'Name':['Ravi','sita','ram','priya'],
    'Age':[22,20,23,21],
    'Marks':[75,95,60,85]
})
# df['Age_plus_5']=df['Age'].apply(lambda x:x+5)
# print(df)

# map()--transforms each value in a seies using a function,dict,mapping series...
# df['Name_upper']=df['Name'].map(str.upper)
# print(df[['Name','Name_upper']])

# apply()with axis=0&axis=1
# axis=1--each row meed operation
# axis=0--each column meeda operation

df['total']=df.apply(lambda row: row['Age']+row['Marks'],axis=1)
print(df[['Name','Age','Marks','total']])