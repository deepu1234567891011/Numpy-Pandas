import pandas as pd
# #reading csv files
# df=pd.read_csv('data.csv')
# #print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())

#redaing excel files
# df=pd.read_excel('excelData.xlsx')
# #print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())

#reading json files 
#df=pd.read_json("json data.json")
#print(df)
#print(df.head())
#print(df.tail())
#print(df.describe())

# df=pd.read_csv("students.csv")
# print(df)
# df=pd.read_csv("students.csv",skiprows=1)
# print(df)

# df=pd.read_csv("students.csv",header=None)
# df=pd.read_csv("students.csv",header=0)
# df=pd.read_csv("students.csv",header=1)
# df=pd.read_csv("students.csv",header=None,names=["id","name","age","city","marks"])
#df=pd.read_csv("students.csv",nrows=3)
# df=pd.read_csv("students.csv",na_values=["NaN ","100"])
# print(df)


#writting files
# df=pd.read_csv("students.csv")
# #df.to_csv("new_students.csv",index=False)
# df[["name", "age"]].to_csv("new_students.csv", index=False)
# print(df[["name", "age"]])

# df=pd.read_csv("students.csv",sep=",")
# print(df)

# df=pd.read_csv("students.csv",header=0)
# print(df)

# df=pd.read_csv("students.csv",header=1) #first row as column name
# print(df)


# df=pd.read_csv("students.csv",skiprows=1)
# print(df)

# df=pd.read_csv("students.csv",nrows=3)
# print(df)


# df=pd.read_csv("students.csv",usecols=["name","age"])
# print(df)

# df=pd.read_csv("students.csv",na_values=["NA"])
# print(df)

# df=pd.read_csv("students.csv",index_col="age")
# print(df)

# writing csv file
df=pd.read_csv("students.csv")
# df.to_csv("News_student.csv",index=False)
# print(df)
# df.to_csv("News_student.csv",sep=":")
# print(df)
# df.to_csv("News_student.csv",header=2)
# print(df)
# df.to_csv("News_students.csv",columns=["name","age"])
# df.to_csv("News_students.csv",na_rep="Missing")
# new_students={
#     "Name":["kiran","sneha"],
#     "age":[21,22],
#     "Marks":[88,89]
# }
# news_df=pd.DataFrame(new_students)
# news_df.to_csv("News_students.csv",mode="a",index=False,header=False)
# print(df)
