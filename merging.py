# Merging means combining two DataFrames using a common column, just like joining two tables in MySQL.

# For example:

# DataFrame 1 contains student names.

# DataFrame 2 contains student marks.

# Both have a common column called student_id.

# import pandas as pd

# students = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "name": ["Ravi", "Sita", "Arun", "Priya"]
# })

# marks = pd.DataFrame({
#     "student_id": [1, 2, 3, 5],
#     "marks": [85, 90, 78, 88]
# })

# result = pd.merge(students, marks, on="student_id")

# print(result)

# Explanation

# pd.merge() — combines two DataFrames.

# students — first DataFrame.

# marks — second DataFrame.

# on="student_id" — matches rows using the common column.

# By default, merge() performs an inner join, so only matching IDs appear.

# Notice that student ID 4 and ID 5 are missing from the output because they don't exist in both DataFrames.

# import pandas as pd
# students=pd.DataFrame({
#     "student_id":[1,2,3,4,5],
#     "name":["Ravi","Sita","Arun","Priya","Kiran"]
# })
# marks=pd.DataFrame({
#     "student_id":[1,2,3,5,6],
#     "marks":[85,92,76,88,81]
# })
# result=pd.merge(students,marks,on="student_id",how="left")
# print(result)
# Left merge keeps all rows from the left DataFrame (student_data.json). If a student has no matching marks, the marks value becomes NaN.


# Right merge keeps all rows from the right DataFrame, which is marks_data.json. Student ID 6 has marks but no matching student details, so name and branch become NaN.
# import pandas as pd
# students = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "name": ["Ravi", "Sita", "Arun", "Priya"]
# })

# marks = pd.DataFrame({
#     "student_id": [1, 2, 3, 5],
#     "marks": [85, 90, 78, 88]
# })

# result = pd.merge(students, marks, on="student_id",how="right")

# print(result)

# Outer merge combines all rows from both DataFrames. Matching rows are combined, and missing values are filled with NaN.”
import pandas as pd
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ravi", "Sita", "Arun", "Priya"]
})

marks = pd.DataFrame({
    "student_id": [1, 2, 3, 5,6],
    "marks": [85, 90, 78, 88,81]
})

result = pd.merge(students, marks, on="student_id",how="outer")
print(result)

