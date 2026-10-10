#Concatenation combines DataFrames by stacking them vertically (rows) or horizontally (columns).
# pd.concat() combines DataFrames.

# axis=0 - combines vertically (rows); this is the default.

# axis=1 - combines horizontally (columns).

# ignore_index=True → resets the output row index.

# import pandas as pd
# df1 = pd.DataFrame({
#     "name": ["Ravi", "Sita"],
#     "marks": [85, 90]
# })

# df2 = pd.DataFrame({
#     "name": ["Arun", "Priya"],
#     "marks": [78, 88]
# })

# result = pd.concat([df1, df2], ignore_index=True)

# print(result)


# import pandas as pd
# df1=pd.DataFrame({
#     "name":["Deepu","Bhanu"],
#     "marks":[85,86]
# })
# df2=pd.DataFrame({
#     "name":["NavyaSri","BhanuSri"],
#     "marks":[88,89]

# })
# result=pd.concat([df1,df2],axis=0,ignore_index=True)
# print(result)

#axis=1 column combines horizontally
import pandas as pd
df1=pd.DataFrame({
    "name":["Deepu","Bhanu"],
    "marks":[85,86]
})
df2=pd.DataFrame({
    "name":["NavyaSri","BhanuSri"],
    "marks":[88,89]

})
result=pd.concat([df1,df2],axis=1,ignore_index=True)
print(result)