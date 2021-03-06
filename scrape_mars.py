#!/usr/bin/env python
# coding: utf-8







# In[1]:


from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
import json


# In[2]:

executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html


# In[4]:


soup = bs(html, 'html.parser')
print(soup.prettify())


# In[5]:


content=soup.find("div",class_="content_page")


# In[6]:


title= content.find_all("div",class_="content_title")
print(title[0].text.strip())


# In[7]:


article= soup.find_all("div",class_="article_teaser_body")
print(article[0].text.strip())


# In[8]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html= browser.html


# In[9]:


soup=bs(html,"html.parser")
featured_image= soup.find("article", class_="carousel_item")["style"]


# In[10]:


latter= featured_image.split('/spaceimages/')[1].split("'")[0]


# In[11]:


former=url.split("?")[0]


# In[12]:


featured_image_url= former + latter
featured_image_url


# In[13]:


facturl= 'https://space-facts.com/mars/'


# In[14]:


table=pd.read_html(facturl)
table[0]


# In[15]:


mars_df = table[0]


# In[16]:


mars_fact_html = mars_df.to_html(header=False, index=False)
mars_fact_html


# In[17]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[18]:


hemisphere_image_urls = []

links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
   
browser.find_by_css("a.product-item h3")[item].click()
    
  
sample_element = browser.find_link_by_text("Sample").first
hemisphere["img_url"] = sample_element["href"]
    
    
hemisphere["title"] = browser.find_by_css("h2.title").text
    
  
hemisphere_image_urls.append(hemisphere)
    
   
browser.back()


# In[19]:


hemisphere_image_urls


# In[ ]:





# In[ ]:

