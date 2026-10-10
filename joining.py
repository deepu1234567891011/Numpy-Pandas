#Pandas join() is commonly used to combine DataFrames based on their index.
# 4 typs of joins
# inner join
# left join
# right join
# outer join

# import pandas as pd
# students=pd.DataFrame({
#     "name":["Ravi","Sita","Arun","Priya","Kiran"],
#     "branch":["CSE","ECE","CSE","IT","ECE"]
# },index=[1,2,3,4,5])
# marks=pd.DataFrame({
#     "marks":[85,92,76,88,81]
# },index=[1,2,3,4,5])
# result=students.join(marks)
# print(result)

# left join
# import pandas as pd

# students = pd.DataFrame({
#     "name": ["Ravi", "Sita", "Arun", "Priya", "Kiran"],
#     "branch": ["CSE", "ECE", "CSE", "IT", "ECE"]
# }, index=[1, 2, 3, 4, 5])

# marks = pd.DataFrame({
#     "marks": [85, 92, 76, 88]
# }, index=[1, 2, 3, 4])

# result = students.join(marks, how="left")

# print(result)

# right join
# import pandas as pd

# students = pd.DataFrame({
#     "name": ["Ravi", "Sita", "Arun", "Priya", "Kiran"],
#     "branch": ["CSE", "ECE", "CSE", "IT", "ECE"]
# }, index=[1, 2, 3, 4, 5])

# marks = pd.DataFrame({
#     "marks": [85, 92, 76, 88]
# }, index=[1, 2, 3, 4])

# result = students.join(marks, how="right")

# print(result)

# outerjoin---Outer join keeps all index values from both DataFrames. 
# If an index doesn't match, the missing values become NaN.

import pandas as pd

students = pd.DataFrame({
    "name": ["Ravi", "Sita", "Arun", "Priya", "Kiran"],
    "branch": ["CSE", "ECE", "CSE", "IT", "ECE"]
}, index=[1, 2, 3, 4, 5])

marks = pd.DataFrame({
    "marks": [85, 92, 76, 88, 81]
}, index=[1, 2, 3, 4, 6])

result = students.join(marks, how="outer")
print(result)

# # inner join--get all matching rowa
# import pandas as pd

# students = pd.DataFrame({
#     "name": ["Ravi", "Sita", "Arun", "Priya", "Kiran"],
#     "branch": ["CSE", "ECE", "CSE", "IT", "ECE"]
# }, index=[1, 2, 3, 4, 5])

# marks = pd.DataFrame({
#     "marks": [85, 92, 76, 88, 81]
# }, index=[1, 2, 3, 4, 6])

# result = students.join(marks, how="inner")

# print(result)