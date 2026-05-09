import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Sales Data.csv")

# Data cleaning
# Removing unnecessary columns
data.drop(columns=["Unnamed: 0","Purchase Address"],inplace=True)

# extract week days from order dates
data["Order Date"]=pd.to_datetime(data["Order Date"],format="%Y-%m-%d %H:%M:%S")
data["Day"]=data["Order Date"].dt.day_name()

# Checking duplicates
data.drop_duplicates(inplace=True)

# Monthly sales data analysis
group1=data.groupby("Month")["Sales"].sum()
most_sales=group1.idxmax()
print(f"Most profitable month is {most_sales} with the sales of {group1[most_sales]} Rs\n")

group2=group1.reset_index().sort_values(by=["Month"],ascending=True)

fig, a=plt.subplots(figsize=(10,5))
a.plot(group2["Month"],group2["Sales"],marker="o",color="tab:blue")
a.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
a.grid()
a.annotate("Most Sales",xy=(most_sales,group1[most_sales]),xytext=(most_sales,group1[most_sales]*1.05),arrowprops=dict(arrowstyle="->"))
a.set_xlabel("Months")
a.set_ylabel("Sales")
a.set_title("Month wise Sales")
plt.savefig("Month_wise_sale.png",dpi=330,bbox_inches="tight")
plt.tight_layout()
plt.show()

# City wise performance
group3=data.groupby("City")["Sales"].sum().sort_values(ascending=False).reset_index()
most_profit_city=group3.iloc[0]
top3=group3.head(3)
print(f"The city with most profit:\n{most_profit_city.to_string()}\n")
print("Top 3 most profitable Cities:")
print(top3.to_string(),"\n")
top3_list=top3["City"].to_list()

# plotting graph
fig, b=plt.subplots(figsize=(10,5))
colors=["tab:orange" if x in top3_list else "tab:blue" for x in group3["City"]]
b.bar(group3["City"],group3["Sales"],color=colors,edgecolor="black")
b.set_title("City wise Revenue")
b.set_xlabel("Cities")
b.set_ylabel("Sales")
b.tick_params(axis="x",rotation=45)
plt.tight_layout()
plt.savefig("city_wise_revenue.png",dpi=330,bbox_inches="tight")
plt.show()

# Best selling time 
group4=data.groupby("Hour")["Order ID"].count()

fig, c=plt.subplots(figsize=(10,5))
c.plot(group4.index,group4.values,color="coral",marker="o")
c.grid()
c.set_xlabel("Hours")
c.set_ylabel("Orders")
c.set_title("Orders For Every Hours")
plt.tight_layout()
plt.savefig("Orders_vs_hours.png",dpi=330,bbox_inches="tight")
plt.show()


peak_hours=group4[group4.values>group4.mean()]
print(f"\nSales are high in the hours {peak_hours.index.min()} to {peak_hours.index.max()}")
print(f"So best time to advertise is around {peak_hours.index.min()-2} to {peak_hours.index.max()} hours")

# Product analysis
group5=data.groupby("Product")["Sales"].sum().sort_values(ascending=False).reset_index()
print("\nTop 3 Most profitable products:")
print(group5.head())

group6=data.groupby("Price Each")["Quantity Ordered"].sum()
fig, d=plt.subplots(figsize=(10,5))
d.scatter(group6.index,group6.values,color="tab:orange",s=100)
d.grid()
d.set_xlabel("Price Each")
d.set_ylabel("Quantity Ordered")
d.set_title("Price and quantity ordered comparision")
plt.tight_layout()
plt.savefig("price_vs_quantity.png",dpi=330,bbox_inches="tight")
plt.show()


most_quantity=group6[group6.values>group6.mean()]
print(f"\nMost Quantity sold in the price range {most_quantity.index.min()} Rs to {most_quantity.index.max()} Rs")





















