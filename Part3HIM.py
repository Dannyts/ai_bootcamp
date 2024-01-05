#!/usr/bin/env python
# coding: utf-8

# HOUSING IN MEXICO PART 3

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# In[ ]:


# Import "data/mexico-real-estate-clean.csv"
df = pd.read_csv("data/mexico-real-estate-clean.csv")

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()


# LOCATION DATA

# In[ ]:


# Use plotly express to create figure
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lon",
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

# Add mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")

# Show figure
fig.show()


# CATEGORICAL DATA

# In[ ]:


#Get value counts of "state" column
df["state"].value_counts().head(10)


# NUMERICAL DATA

# In[ ]:


# Describe "area_m2", "price_usd" columns
df[["area_m2", "price_usd"]].describe()


# In[ ]:


# Use Matplotlib to create histogram of "area_m2"
plt.hist(df['area_m2'])

# Add x-axis label
plt.xlabel("Area [sq meters]")

# Add y-axis label
plt.ylabel("Frequency")

# Add title
plt.title("Distribution of Home Sizes");


# In[ ]:


# Use Matplotlib to create boxplot of "area_m2"
plt.boxplot(df["area_m2"], vert= False)

# Add x-axis label
plt.xlabel("Area [sq meters]")

# Add title
plt.title("Distribution of Home Sizes");


# In[ ]:


# Use Matplotlib to create histogram of "price_usd"
plt.hist(df["price_usd"])

# Add x-axis label
plt.xlabel("Price [USD]")

# Add y-axis label
plt.ylabel("Frequency")

# Add title
plt.title("Distribution of Home Prices");


# In[ ]:


# Use Matplotlib to create boxplot of "price_usd"
plt.boxplot(df["price_usd"], vert=False)

# Add x-label axis
plt.xlabel("Price [USD]")

# title
plt.title("Distribution of Home Prices");

