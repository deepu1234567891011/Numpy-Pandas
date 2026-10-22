import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
# print(df.head())
# print(df.shape)returns a no.of nows & colums
# print(df.info())prints datatypes,on-null counts
# print(df.columns)
# print(df.tail())if we want last five values
# print(df.describe())if we want statical values
# print(df.isnull())
# isnull used to idnetify missing values in a df or series it return true for missig values and false for non-missing values..
# print(df.isnull().sum())
# sum method counts the true values returned  by isnull 

# fiding average math score
print("Average Math score is....",df["math score"].mean())
# findig average reading score
print("Average Reading score is...",df["reading score"].mean())
# finding average writing score
print("Average writing score is...",df["writing score"].mean())

# finding the highest math score
print("Highest Math Score is..",df["math score"].max())

# find the studnet who scored the highest in math score
top_student=df.loc[df["math score"].idxmax()]
print("students with highest score in math",top_student)

# find the student with the highest reading score
top_reading=df.loc[df["reading score"].idxmax()]
print("students with highest score in reading",top_reading)

# find the student with the highest writing score
top_writing=df.loc[df["writing score"].idxmax()] 
print("students with highest score in writing",top_writing)

# sort studets by math score--ascending=false highest to lowest
sorted_df=df.sort_values(by="math score",ascending=False)
print(sorted_df[["gender","math score"]].head(15))

# filter students with math score>=80
high_math=df[df["math score"]>=80]
print(high_math[["gender","math score"]])

# gender wise average math score
gender_avg=df.groupby("gender")["math score"].mean()
print(gender_avg)

# calculate the total score of each student
df["total_score"]=(df["math score"]+df["reading score"]+df["writing score"])
print(df[["math score","reading score","writing score","total_score"]])

# create an average score column
df["average_score"]=(df[["math score","reading score","writing score"]].mean(axis=1))
print(df[["math score","reading score","writing score","average_score"]].head())

# find the top 10 students
top_10=df.sort_values(by="average_score",ascending=False).head(10)
print(top_10)

# find the students who scored below 40 in math
below_40=df[df["math score"]<40]
print(below_40)

# gender wise student count
gender_count=df["gender"].value_counts()
print(gender_count)

# save the cleaned dataset
df.to_csv("StudentsPerformance.csv",index=False)
print("Dataset saved successfully!!!")