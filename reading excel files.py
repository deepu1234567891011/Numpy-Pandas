# import pandas as pd
# df=pd.read_excel("excelData.xlsx")
# print(df)
#redaing excel files
# df=pd.read_excel("excelData.xlsx",sheet_name=1)
# print(df)
# df=pd.read_excel("excelData.xlsx",header=1)
# print(df)
# df=pd.read_excel("students data.xlsx",header=0)
# print(df)
# df=pd.read_excel("students data.xlsx",usecols=["ID","Name"])
# print(df)
# excel = pd.ExcelFile("students data.xlsx")

# print(excel.sheet_names)
# df=pd.read_excel("students data.xlsx")
# print(df.head())

# import pandas as pd

# df = pd.read_excel(
#     "students data.xlsx",
#     sheet_name="Student Marks",
#     header=None
# )

# print(df.to_string())

# import pandas as pd
# df=pd.read_excel("collegeexamresults.xlsx")
# print(df)

# df=pd.read_excel("collegeexamresults.xlsx",sheet_name="Attendance")
# print(df)

# df=pd.read_excel("collegeexamresults.xlsx",sheet_name=None)
# print(df)

# import pandas as pd

# df = pd.ExcelFile("collegeexamresults.xlsx",sheet_name=0)

# print(df)



# df=pd.read_excel("collegeexamresults.xlsx")
# print(df.head())
# print(df.tail())
# print(df.describe())
# df=pd.read_excel("collegeexamresults.xlsx",sheet_name=6)
# print(df)

import pandas as pd

# excel = pd.ExcelFile("collegeexamresults.xlsx")

# print(excel.sheet_names)

# df = pd.read_excel("collegeexamresults.xlsx", sheet_name=0)

# print(df)

import pandas as pd
# df=pd.read_excel("collegeexamresults.xlsx",header=2)
# df=pd.read_excel("collegeexamresults.xlsx",
#                  usecols=["Student_ID","Attendance","SQL_Marks"])
# df=pd.read_excel("collageexamresults.xlsx",usecols="A,B")
# df=pd.read_excel("collegeexamresults.xlsx",skiprows=4)
# df=pd.read_excel("collegeexamresults.xlsx",nrows=5)
# df=pd.read_excel("collegeexamresults.xlsx")
# df=pd.read_excel("collegeexamresults.xlsx",index_col="Student_ID")
# df=pd.read_excel("collegeexamresults.xlsx",
#                  dtype={
#         "Student ID": str,
#         "Python_Marks": int
#     }
# )
# df = pd.read_excel(
#     "collegeexamresults.xlsx",
#     na_values=["NA", "N/A", "null", "-", "missing"]
# )


# print(df)

