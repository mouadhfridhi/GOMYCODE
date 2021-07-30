#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd 
df = pd.read_csv('C:\\Users\\Pc\\Desktop\\Gomycode\\gomycode project.csv', sep=',')
df


# In[102]:


df.isnull().sum()


# In[103]:


df.columns


# In[104]:


df['Engine']


# In[105]:


len(df)


# In[106]:


df['Engine']=df['Engine'].str.replace(" CC","")


# In[107]:


df['Power']=df['Power'].str.replace('bhp','')


# In[108]:


df['Mileage']=df['Mileage'].str.replace('km/kg','')


# In[109]:


df['Mileage']=df['Mileage'].str.replace('kmpl','')


# In[110]:


df


# In[111]:


df.isnull().sum()


# In[112]:


df['Fuel_Type'].unique()


# In[113]:


df['Transmission'].unique()


# In[114]:


df['Owner_Type'].unique()


# In[115]:


Cleanup_nums0={
    
    "Fuel_Type" : {"CNG":0, "Diesel":1, "Petrol":2, "LPG":3, "Electric":4}
}
df.replace(Cleanup_nums0, inplace= True)


# In[116]:


Cleanup_nums1={
    
    "Owner_Type" : {"First":1, "Second":2, "Third":3, "Fourth & Above":4}
}
df.replace(Cleanup_nums1, inplace= True)


# In[117]:


from sklearn.preprocessing import LabelEncoder
one_hot=pd.get_dummies(df['Transmission'])
df=df.drop('Transmission', axis=1)
df=df.join(one_hot)


# In[118]:


df


# In[134]:


df.isnull().sum()


# In[121]:


df['Seats'].fillna(df['Seats'].mean(), inplace=True)


# In[124]:


df['Price'].fillna(df['Price'].mean(), inplace=True)


# In[131]:


pd.to_numeric(df['Engine'])


# In[132]:


df['Engine'].unique()


# In[133]:


df['Engine'].fillna(df['Engine'].mean(), inplace=True)


# In[ ]:





# In[ ]:




