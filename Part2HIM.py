#!/usr/bin/env python
# coding: utf-8

# HOUSING IN MEXICO PART 2

# In[ ]:


import pandas as pd


# In[ ]:


# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")

# Print object type and shape for DataFrames
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
print()
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
print()
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)


# CLEAN DF1

# In[ ]:


# Print df1 shape

df1.shape
# Print df1 info
df1.info()

# Get output of df1 head
df1.head()


# In[ ]:


# Drop null values from df1
df1.dropna(inplace=True)

# Clean "price_usd" column in df1
df1["price_usd"] = df1["price_usd"].str.replace("$","",regex=False).str.replace(",","").astype(float)

# Print object type, shape, and head
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
df1.head()


# CLEAN DF2

# In[ ]:


# Drop null values from df2
df2.dropna(inplace=True)

# Create "price_usd" column for df2 (19 pesos to the dollar in 2014)
df2["price_usd"] = (df2["price_mxn"]/19).round(2)

# Drop "price_mxn" column from df2
df2.drop(columns=["price_mxn"], inplace= True)

# Print object type, shape, and head
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
df2.head()


# CLEAN DF3

# In[ ]:


# Drop null values from df3
df3.dropna(inplace=True)

# Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)

# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
df3.head()


# In[ ]:


# Create "state" column for df3
df3["state"] = df3["place_with_parent_names"].str.split("|", expand=True)[2]

# Drop "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names", "lat-lon"], inplace=True)

# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
df3.head()


# CONCATENATE

# In[ ]:


# Concatenate df1, df2, and df3
df = pd.concat([df1, df2, df3])

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()


# In[ ]:


SAVE


# In[ ]:


# Save df
df.to_csv("data/mexico-real-estate-clean.csv", index=False)

