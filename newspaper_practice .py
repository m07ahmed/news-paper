#!/usr/bin/env python
# coding: utf-8

# # import necessaery libraries

# In[40]:


import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns


# # import data

# In[41]:


newspaper_data = pd.read_csv('newspaperdata.csv')
newspaper_data 


# # data understanding

# ### Initial Analysis

# In[13]:


newspaper_data.shape


# In[14]:


newspaper_data.isna().sum()


# In[15]:


newspaper_data.dtypes


# # Perform assumption test

# # 1.Linearity test

# In[42]:


sns.scatterplot(x='daily',y='sunday',data=newspaper_data )
plt.title('daily Vs sunday')
plt.show


# In[43]:


sns.lmplot(x='daily',y='sunday',data=newspaper_data)
plt.title('daily vs sunday')
plt.show()


# In[20]:


sns.distplot(a=newspaper_data['daily'],hist=False)
plt.title('daily distribution')
plt.show


# In[21]:


newspaper_data


# In[32]:


del newspaper_data['Newspaper']


# In[33]:


newspaper_data.head()


# In[34]:


newspaper_data.dtypes


# In[35]:


newspaper_data.isna().sum()


# In[46]:


import statsmodels.formula.api as smf


# In[55]:


smf.ols('sunday ~ daily',data=newspaper_data)


# In[60]:


linear_model = smf.ols(formula = 'sunday~daily',data = newspaper_data).fit()
linear_model


# In[61]:


linear_model.params


# In[ ]:




