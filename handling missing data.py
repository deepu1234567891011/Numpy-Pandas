import pandas as pd
import numpy as np
df=pd.read_json("students.json")
df.loc[2, "marks"] = np.nan
df.loc[5, "city"] = np.nan
df.loc[7, "age"] = np.nan
# print(df)
# isna() is used to check whether a value is missing or not.
# syntax:df.isna()
# true--value missing,false--value not missing
# print(df.isna())#get true as output when it having nan in data
# print(df.isnull())#same as isna
# 2.count missing values---isna tells where the missing values are
# But if we want to know how many missing values are present in each column, use:isna().sum()
# isna().sum() is used to count the number of missing values in each column of a DataFrame.
# print(df.isna().sum())


# 3.find rows containing missing values
# we can find rowss constaining missing values using syntax:df.isna().any(axis=1)
# axis 1 means row wise--find rows that have at least one missing value
# axis 0 means column wise
# print(df[df.isna().any(axis=1)])


# 4.Remove Missing values--dropna()
# dropna()--is used to remove rows or columns containing missing values from a dataframe..
# by default it removes rows that constain at least one nan
# print(df.dropna())

# 5.dropna() with how
# how tells pandas when to remove a row/column
# how=any--if at least one value is nan in row remove that entire row
# print(df.dropna(how="any"))
# how=all---remove the row only when all values are missing--row will removed
# print(df.dropna(how="all"))

# 6.dropna() with subset
# subset is used with dropna() to specify which column or columns should
# be checked for missing values
# print(df.dropna(subset=["marks"]))

# 7.fill missing values--fillna()
# fillna is used to replace missing values with a specified value in a pandas Dataframe
# df["city"]=df["city"].fillna("chennai")
# print(df)
# df["marks"]=df["marks"].fillna(50)
# print(df)


# 8.fill missing values with mean()
# df["marks"]=df["marks"].fillna(df["marks"].mean())
# print(df)
# missing values with median()
# df["marks"]=df["marks"].fillna(df["marks"].median())
# print(df)
# missing values with mode()
# df["city"]=df["city"].fillna(df["city"].mode())
# print(df)

# 9.Forward fill-ffill()
# fills missing values using the previous available value
# sntax:df["city"]=df["city"].ffill()
# df["city"]=df["city"].ffill()
# print(df)

# 10 backward fill-bfill()
# fills missing values using the next available value
# df["city"]=df["city"].bfill()
# print(df)

# 11 replace missing values in specific columns
# we can handle missing values differently for different columns based on the data type business requirements..


