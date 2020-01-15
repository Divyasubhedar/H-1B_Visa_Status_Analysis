#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


import os


# In[3]:


print(os.listdir("D:\Github Projects\Tableau")) #give the dir of file


# In[5]:


df2017 = pd.read_excel(r'D:\Github Projects\Tableau\H-1B_Disclosure_2017.xlsx')#location of excel


# In[6]:


df2018 = pd.read_excel(r'D:\Github Projects\Tableau\H-1B_Disclosure_2018.xlsx')#location of excel


# In[7]:


df2017.columns #all clolumns from 2017 file


# In[8]:


df2017.CASE_STATUS.value_counts() #Count of case status 2017 year


# In[9]:


df2018.CASE_STATUS.value_counts() #Count of case status 2018 (As compare to 2017 deniel rate is decreased in 2018)


# In[10]:


use_cols= ['CASE_NUMBER', 'CASE_STATUS', 'CASE_SUBMITTED', 'DECISION_DATE',
       'EMPLOYMENT_START_DATE', 'EMPLOYER_NAME',  'EMPLOYER_CITY', 'EMPLOYER_STATE',
       'JOB_TITLE', 'SOC_CODE', 'SOC_NAME',  'PREVAILING_WAGE', 'PW_UNIT_OF_PAY',
       'PW_WAGE_LEVEL', 'WAGE_RATE_OF_PAY_FROM', 'WAGE_RATE_OF_PAY_TO', 'WAGE_UNIT_OF_PAY',
       'WORKSITE_CITY', 'WORKSITE_STATE']

df2018_New = df2018[use_cols][(((((df2018.CASE_STATUS =='CERTIFIED') |(df2018.CASE_STATUS =='DENIED')) 
                             & (df2018.VISA_CLASS =='H-1B'))
                            &(df2018.CHANGE_EMPLOYER !=0))
                           &(df2018.EMPLOYER_COUNTRY =='UNITED STATES OF AMERICA'))
                                &(df2018.FULL_TIME_POSITION =='Y')]
df2017_New = df2017[use_cols][(((((df2017.CASE_STATUS =='CERTIFIED') |(df2017.CASE_STATUS =='DENIED')) 
                             & (df2017.VISA_CLASS =='H-1B'))
                            &(df2017.CHANGE_EMPLOYER !=0))
                           &(df2017.EMPLOYER_COUNTRY =='UNITED STATES OF AMERICA'))
                                &(df2017.FULL_TIME_POSITION =='Y')]
                              


# In[11]:


df2017_New.head(4)


# In[15]:


# Here you can see the jobtitles which are certified from amazon
df2018_New.JOB_TITLE[(df2018_New.EMPLOYER_NAME.str.contains("Amazon",case=False)==True)&(df2018_New.CASE_STATUS =='CERTIFIED')].value_counts() 


# In[16]:


#Here you can see count of employers from google.
df2018.EMPLOYER_NAME[df2018.EMPLOYER_NAME.str.contains('GOOGLE',case=False) == True].value_counts() 


# In[17]:


#Certifies job positions from Facebook.
df2018.JOB_TITLE[(df2018.EMPLOYER_NAME.str.contains("FACEBOOK",case=False)==True)&(df2018.CASE_STATUS =='CERTIFIED')].value_counts()

