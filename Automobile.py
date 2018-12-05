
# coding: utf-8

# In[47]:


import os 
os.chdir("C:/Users/hp/Desktop")
os.getcwd()


# In[48]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


df = pd.read_csv("Automobile_data.csv")


# In[50]:


ls


# In[51]:


df["normalized-losses"].value_counts()


# In[52]:


df1 = pd.DataFrame(df)


# In[53]:


df1


# In[54]:


nl = df1["normalized-losses"].loc[df1["normalized-losses"]!="?"]


# In[55]:


nl


# In[56]:


nl = nl.astype(str).astype(int).mean()


# In[57]:


nl


# In[58]:


df1["normalized-losses"]=df1["normalized-losses"].str.replace("?",str(nl))


# In[59]:


df1["normalized-losses"]=df1["normalized-losses"].astype(float)


# In[60]:


df1["normalized-losses"].describe()


# In[61]:


df1.dtypes


# In[62]:


p = df["price"].loc[df["price"]!="?"]


# In[63]:


p1=p.median()


# In[64]:


df["price"] = df["price"].str.replace("?",str(p1))


# In[65]:


df["price"] = df["price"].astype(float)


# In[66]:


p1


# In[67]:


df["price"].describe()


# In[68]:


L = df["horsepower"].loc[df["horsepower"]!="?"]


# In[69]:


L1=L.median()


# In[70]:


df["horsepower"] =df["horsepower"] .str.replace("?",str(L1))


# In[71]:


df["horsepower"] =df["horsepower"].astype(float)


# In[72]:


df["horsepower"] .describe()


# In[73]:


df["horsepower"].value_counts()


# In[74]:


rp = df["peak-rpm"].loc[df["peak-rpm"]!="?"]


# In[75]:


rp1 =rp.astype(str).astype(int).mean() 


# In[76]:


df["peak-rpm"] = df["peak-rpm"].str.replace("?",str(rp1))


# In[77]:


df["peak-rpm"] = df["peak-rpm"].astype(float)


# In[78]:


df["peak-rpm"].describe()


# In[79]:


L1


# In[80]:


rp1


# In[81]:


df["bore"] = pd.to_numeric(df["bore"],errors="coerce")


# In[82]:


df["bore"].value_counts()


# In[83]:


df["bore"].count()


# In[84]:


df["stroke"].value_counts()


# In[85]:


df["stroke"] = pd.to_numeric(df["stroke"],errors="coerce")


# In[86]:


df["stroke"].count()


# In[87]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[88]:


df["make"].value_counts().nlargest(5).plot(kind="bar")


# In[89]:


df["normalized-losses"].plot(kind="bar")


# In[104]:


[df["bore"].fillna(df["bore"].median(),inplace = True)]


# In[91]:


df["fuel-type"].value_counts().plot()


# In[92]:


df["aspiration"].value_counts().plot.pie(autopct = "%.2f")


# In[93]:


df["fuel-type"].value_counts().plot.pie(autopct = "%.2f")


# In[94]:


df["drive-wheels"].value_counts().plot.pie(autopct = "%.2f")


# In[95]:


df["horsepower"].value_counts().hist(bins = 6)
plt.title("Horse power graph")
plt.ylabel("Number of Vehicles")
plt.xlabel("HP")


# In[96]:


df["engine-size"].value_counts().hist(bins = 6)


# In[97]:


corr = df.corr()


# In[98]:


corr


# In[99]:


sns.set_context("notebook",font_scale = 1.0)
plt.figure(figsize=(13,7))
a = sns.heatmap(corr , annot = True , fmt = ".2f")


# In[100]:


g = sns.lmplot("price","engine-size",df)


# In[101]:


g = sns.lmplot("normalized-losses","symboling",df)


# In[102]:


g = sns.lmplot("city-mpg","curb-weight",df, hue = "make",fit_reg = False)


# In[103]:


plt.rcParams["figure.figsize"]=(23,10)
ax = sns.boxplot(x="make",y="price",data = df1)

