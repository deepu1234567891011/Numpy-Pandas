import pandas as pd
df=pd.read_json("students.json")
# print(df)
# print(df.columns)
#selecting one column
# print(df["name"])
# print(df.age)
#selectig multiple columns
# print(df[["name","age"]])
# print(df[["name","age","branch","marks"]])
#selecting one row
# print(df.iloc[0])
# print(df.iloc[0:3])
#selecting  row+column with value
# print(df.iloc[0,1])#first row 2rd column value
#print(df.iloc[1,3])
# print(df.iloc[2,4])
# select rows+columns
# print(df.iloc[0:3,1:4])
#select data by labels
# print(df.loc[0])
#select row+column with label
# print(df.loc[0,"name"])
#select all rows multiple columns
# print(df.loc[:,["name","age"]])
#selcet multiple rows+colims
# print(df.loc[1:2,["name","age"]])

#filtering rows
# Filtering in Pandas is used to select rows that satisfy a specific condition."
# Comparison Operators in Filtering (>, <, >=, <=, ==, !=).
# print([df["marks"]>80])
# print([df["marks"]<80])
# print([df["marks"]>=80])
# print([df["marks"]<=80])
# print(df["marks"]==80)
# print(df["marks"]!=80)

# filtering with multiple conditions
# print(df[(df["marks"] > 80) & (df["branch"] == "CSE")])

# print(df[(df["branch"] == "CSE") | (df["branch"] == "IT")])

# print(df[~(df["branch"] == "CSE")])

# print(df[(df["marks"]>75) &(df["age"]>21)])

# print(df[(df["branch"] == "CSE") | (df["branch"] == "IT")])


# print(df[df["city"] != "Hyderabad"])

# isin() — Filtering Multiple Values
# isin() is used to filter rows by checking whether values belong to a given list.
# syntax df[df["column"].isin([value1, value2])]
# print(df[df["city"].isin(["Hyderabad", "Guntur"])])

# print(df[~df["city"].isin(["Hyderabad", "Guntur"])])#reverse the condition how are not from hyd and gnt
# isin() is a Pandas method used to filter rows by checking whether column values are present in a specified list."


# 9. between() — Range Filtering
# between() is used to filter rows where a column's values fall within a specified range.
# sntax df[df["column"].between(start, end)]
# print(df[df["marks"].between(70, 90)])

# String Filtering
# String filtering ante text column lo specific text ni search chesi rows filter cheyyadam.

# Main 3 methods:

# str.contains()
# str.startswith()
# str.endswith()

#print(df[df["city"].str.contains("Hyd")])
# print(df[df["name"].str.startswith("S")])
# print(df[df["name"].str.endswith("i")])

# Pandas string methods such as str.contains(), str.startswith(), and str.endswith() are used to filter rows based on text values."


# 11.Conditional Selection using loc[]
# loc[] ni filtering condition tho combine chesi condition satisfy ayye rows lo specific columns select cheyyachu.

# syntax df.loc[condition, ["column1", "column2"]]
# print(df.loc[df["marks"] > 80, ["name", "marks"]])
#multiple conditions
# "loc[] can be used with a condition to filter rows and select specific columns at the same time."

# 12.query() — SQL-like Filtering

# syntax df.query("condition")
# norml filtering 
# print(df[df["marks"] > 80])

#multiple conditions
# print(df.query("marks > 80 and age > 21"))