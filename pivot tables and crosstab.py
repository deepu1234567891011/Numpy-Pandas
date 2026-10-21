# pivot_table()--a pivot table summarizes data by grouping rows and columns&applying an 
# aggregation function such as sum,mean,count
import pandas as pd
df=pd.DataFrame({
    'Name':['Ravi','Sita','Ram','Priya','john'],
    'Department':['IT','HR','IT','HR','IT'],
    'Gender':['Male','Female','Male','Female','Male'],
    'Marks':[75,95,60,85,90]
})
# result=pd.pivot_table(df,values='Marks',index='Department',aggfunc='mean')
# print(result)
# result=pd.pivot_table(df,values='Marks',index='Department',columns='Gender',aggfunc='mean')
# print(result)


# crosstab()--cretaes a frequency table showig the count of combinations between categorical variables
result=pd.crosstab(df['Department'],df['Gender'])
print(result)
