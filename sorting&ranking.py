# sorting is the process of arranging rows in a dataframe based o column values or index labels in ascending or descendig order

import pandas as pd
df=pd.DataFrame({
    'Name':['Ravi','sita','ram','priya'],
    'Age':[22,20,23,21],
    'Marks':[75,95,60,85]
})
# print(df)

# sort_values()--method sorts a df based on one or more column values
# arrange in small to big
# print(df.sort_values('Marks',ascending=True))
# descending order-bigtosmall
# print(df.sort_values('Marks',ascending=False))


# sorting by multiple columns
# we can sort a dataframe using multiple columns and specify the sorting order for each column
# print(df.sort_values(['Age','Marks'],ascending=[True,False]))

# sort_index()--method sorts a df based on its index labels..
# print(df.sort_index(ascending=False))

# Ranking--assigns a rank to each value in a series based on its position relative to other values
# df['Rank']=df['Marks'].rank(ascending=False)
# print(df)

# ranking methods
# average--equal values ki average rank default
# max---equal values ki largest rank
# min--equal vlues ki smallst rank
# first--data lo first ga vachia value ni first rank
# dense--equal ranks tharuvta gape lekuda ranks assign chestundhi
df['Marks'].rank(method='average',ascending=False)
df['Marks'].rank(method='max',ascending=False)
df['Marks'].rank(method='min',ascending=False)
df['Marks'].rank(method='first',ascending=False)
df['Marks'].rank(method='dense',ascending=False)
print(df)
