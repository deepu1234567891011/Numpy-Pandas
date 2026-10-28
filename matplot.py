# import matplotlib.pyplot as plt
# days=[1,2,3,4,5]
# marks=[10,40,30,60,25]
# plt.scatter(days,marks)
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "attdence":[97,80,85,99,87],
#     "marks":[80,97,87,100,90]
# }
# df=pd.DataFrame(data)
# plt.scatter(df["attdence"],df["marks"])
# plt.show()

# adding a title and axis labels
# title---adds title to the graph
# axis---data is plotted inside the figure it includes x-axis,y-axis
# x-labels means add a label to x-axis
# y-labels mans add a label to y-axis
# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "days":[1,2,3,4,5],
#     "marks":[10,40,20,49,68]

# }
# df=pd.DataFrame(data)
# plt.plot(df["days"],df["marks"])
# plt.title("Students marks analysis")
# plt.xlabel("student number")
# plt.ylabel("student marks")
# plt.show()


# task
# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "Product":["Laptop","Mobile","Tablet","Headphone"],
#     "sales":[50,80,40,60]
# }
# df=pd.DataFrame(data)
# df.plot(x="Product",y="sales",kind="bar")
# plt.title("Product sales analysis")
# plt.xlabel("Product")
# plt.ylabel("sales")
# plt.show()


# figsize--controls the width and height
# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "Product":["Laptop","Mobile","Tablet","Headphone"],
#     "sales":[50,80,40,60]
# }
# df=pd.DataFrame(data)
# df.plot(x="Product",y="sales",kind="bar",figsize=(8,5))
# plt.title("Product sales analysis")
# plt.xlabel("Product")
# plt.ylabel("sales")
# plt.show()

# colors,marker,line styles
# colors
# marker--show individual data points on a chart
# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "Product":["Laptop","Mobile","Tablet","Headphone"],
#     "sales":[50,80,40,60]
# }
# df=pd.DataFrame(data)
# df.plot(x="Product",y="sales",
#         kind="line",color="red",
#         marker="o",linestyle="--",figsize=(8,5))
# plt.title("Product sales analysis")
# plt.xlabel("Product")
# plt.ylabel("sales")
# plt.show()

# save charts with plt.savefig()

# histogram charts
# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "Product":["Laptop","Mobile","Tablet","Headphone"],
#     "sales":[100,80,40,20]
# }
# df=pd.DataFrame(data)
# df["sales"].plot(kind="hist",bins=4,color="green",
#                  edgecolor="black",alpha=0.7,figsize=(8,5))
# plt.title("Product sales analysis")
# plt.xlabel("Product")
# plt.ylabel("sales")
# plt.grid(axis="y")
# plt.show()


# pie chart
import matplotlib.pyplot as plt
import pandas as pd
data={
    "Products":["Laptop","Mobile","Tablet","Headphone"],
    "sales":[50,80,40,60]
}
df=pd.DataFrame(data)
df=df.set_index("Products")
df["sales"].plot(kind="pie",autopct="%1.1f%%",
               colors=["skyblue","orange","lightgreen","pink"],
               startangle=90,figsize=(7,7))
plt.title("Products sales analysis")
plt.ylabel("")
plt.show()
# autopct--display each product percentage
# startangle--rotates the charts 90degrees
# y.label()--remove unnexxessary labels