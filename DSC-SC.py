#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[7]:


data=pd.read_csv("D:\student_extended_ml_dataset2.csv")


# In[8]:


data.head()


# In[9]:


data.tail()


# In[12]:


data.shape


# In[13]:


data.describe()


# In[15]:


data.columns


# In[16]:


data.nunique


# In[17]:


data['Gender'].unique()


# In[18]:


data['IQ'].unique()


# In[20]:


data['Chemistry_Marks'].unique()


# In[ ]:


#cleaning the database


# In[21]:


data.isnull().sum()


# In[23]:


student=data.drop(['Gender','Has_Part_Time_Job'],axis=1)


# In[27]:


student.head()


# In[ ]:


#relationship analysis


# In[ ]:


#corelation matrix


# In[26]:


corelation = student.corr()


# In[28]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns
           ,annot=True)


# In[29]:


sns.pairplot(student)


# In[30]:


sns.relplot(x='Physics_Marks',y='Math_Marks',hue='IQ',data=student)


# In[32]:


sns.relplot(x='Physics_Marks',y='Math_Marks',hue='Age',data=student)


# In[35]:


sns.distplot(student['Physics_Marks'])


# In[36]:


sns.displot(student['Physics_Marks'])


# In[39]:


sns.histplot(student['Math_Marks'])


# In[40]:


sns.histplot(student['Age'])


# In[41]:


sns.distplot(student['Age'])


# In[42]:


sns.histplot(student['Hours_Studied'])


# In[43]:


sns.distplot(student['Hours_Studied'])


# In[44]:


sns.histplot(student['Hours_Studied'],bins=10)


# In[45]:


sns.catplot(x='Physics_Marks',kind='box',data=student)


# In[46]:


sns.catplot(x='Age',kind='box',data=student)


# In[47]:


sns.catplot(x='Hours_Studied',kind='box',data=student)


# In[ ]:




