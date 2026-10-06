import pandas as pd
df=pd.read_json("students.json")
# 1.sort_values()
# sort values is used to sort rows based on a columns values
# df=df.sort_values("marks",ascending=False)large to small
# df=df.sort_values("marks",ascending=True)small to big
# print(df)

# 2.sorted by multiple columns
df=df.sort_values(by=["branch","marks"],ascending=[True,False])
print(df)
