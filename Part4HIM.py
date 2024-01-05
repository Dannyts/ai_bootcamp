#!/usr/bin/env python
# coding: utf-8

# In[ ]:


HOUSING IN MEXICO P4


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd


# IMPORT DATA

# In[ ]:


# Import "data/mexico-real-estate-clean.csv"
df = pd.read_csv("data/mexico-real-estate-1.csv")
df["price_usd"] = (
    df["price_usd"]
    .str.replace("$","", regex=False)
    .str.replace(",","")
    .astype(float))

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()


# In[ ]:


MOST EXPENSIVE STATE


# In[ ]:


# Declare variable `mean_price_by_state`
mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values(ascending=False)

# Print object type, shape, and head
print("mean_price_by_state type:", type(mean_price_by_state))
print("mean_price_by_state shape:", mean_price_by_state.shape)
mean_price_by_state.head()


# In[ ]:


# Create bar chart from `mean_price_by_state` using pandas
mean_price_by_state.plot(
    kind="bar",
    xlabel="State",
    ylabel="Price [USD]",
    title="Mean House Price by State"
);


# In[ ]:


# Create "price_per_m2" column
df["price_per_m2"] = df["price_usd"]/df["area_m2"]

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()


# In[ ]:


# Group `df` by "state", create bar chart of "price_per_m2"
(
    df
    .groupby("state")
    ["price_per_m2"].mean()
    .sort_values(ascending=False)
    .plot(
        kind="bar",
        xlabel="State",
        ylabel="Mean Price pero sq meter [USD]",
        title="Mean House Price per sq meter by State"
     )
);


# RELATION BETWEEN SIZE AND PRICE

# In[ ]:


# Create scatter plot of "price_usd" vs "area_m2"
plt.scatter(x=df["area_m2"], y=df["price_usd"])

# Add x-axis label
plt.xlabel("Area [sq meters]")

# Add y-axis label
plt.ylabel("Price [USD]")

# Add title
plt.title("Price vs Area");


# In[ ]:


# Calculate correlation of "price_usd" and "area_m2"
p_correlation = df["area_m2"].corr(df["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)


# In[ ]:


# Declare variable `df_morelos` by subsetting `df`
df_morelos = df[df["state"] == "Morelos"]

# Print object type, shape, and head
print("df_morelos type:", type(df_morelos))
print("df_morelos shape:", df_morelos.shape)
df_morelos.head()


# In[ ]:


# Create scatter plot of "price_usd" vs "area_m2" in Morelos
plt.scatter(x=df_morelos["area_m2"], y=df_morelos["price_usd"])

# Add x-axis label
plt.xlabel("Area [sq meters]")

# Add y-axis label
plt.ylabel("Price [USD]")

# Add title
plt.title("Morelos: Price vs Area");


# In[ ]:


# Calculate correlation of "price_usd" and "area_m2" in `df_morelos`
p_correlation = df_morelos["area_m2"].corr(df_morelos["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (Morelos):", p_correlation)


# In[ ]:


# Declare variable `df_mexico_city` by subsetting `df`
df_mexico_city = df[df["state"] == "Distrito Federal"]

# Print object type and shape
print("df_mexico_city type:", type(df_mexico_city))
print("df_mexico_city shape:", df_mexico_city.shape)

# Create a scatter plot "price_usd" vs "area_m2" in Distrito Federal
plt.scatter(df_mexico_city["area_m2"], df_mexico_city["price_usd"])  

# Add x-axis label
plt.xlabel("Area [sq meters]")  

# Add y-axis label
plt.ylabel("Price [USD]") 

# Add title
plt.title("Mexico City: Price vs. Area")  

# Calculate correlation of "price_usd" and "area_m2" in `df_mexico_city`
p_correlation = df_mexico_city["area_m2"].corr(df_mexico_city["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (Mexico City):", p_correlation)

