#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# Useragent URL will be different for every PC chrome

# In[2]:


headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}


# Yahoo Finance API Pricing URL

# In[3]:


URL = 'https://finance.yahoo.com/quote/F'


# REST API call

# In[4]:


r = requests.get(URL)


# In[5]:


print(r.status_code)


# In[6]:


soup = BeautifulSoup(r.text, 'html.parser')


# Yahoo Finance API JSON class details

# In[7]:


price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text
change = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text


# Last Price Details of the Instrument's

# In[8]:


print(price, change)

