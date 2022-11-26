#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs


# In[3]:


import requests


# In[4]:


link="https://www.flipkart.com/google-pixel-7-snow-128-gb/p/itm45d75002be0e7?pid=MOBGHW44PRZ8WP2M&lid=LSTMOBGHW44PRZ8WP2MEGIXNO&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_3&otracker=hp_bannerads_1_2.bannerAdCard.BANNERADS_Cat-Mob-HPW2-Pixel%2B7-_OI204387L9YV&fm=neo%2Fmerchandising&iid=b72a85a6-eaf9-476e-adad-fb9bf1c7acf0.MOBGHW44PRZ8WP2M.SEARCH&ppt=hp&ppn=homepage&ssid=6512vadlsg0000001669195963995"


# In[5]:


page=requests.get(link)


# In[7]:


page


# In[11]:


page.content


# In[13]:


soup=bs(page.content,"html.parser")
soup


# In[15]:


print(soup.prettify())


# # Title of the Product

# In[17]:


title=soup.title


# In[19]:


print(soup.title)


# In[21]:


print(type(soup))


# In[23]:


print(title.string)


# # Check Product Price

# In[27]:


price=soup.find_all("div",class_="_30jeq3 _16Jk6d")


# In[29]:


price


# In[32]:


product_price=[]

for i in range(0,len(price)):
    product_price.append(price[i].get_text())


# In[34]:


product_price


# In[36]:


price[i].get_text()


# # Scrap Customer Names

# In[38]:


names=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
names


# In[40]:


cust_name=[]

for i in range(0,len(names)):
    cust_name.append(names[i].get_text())


# In[42]:


cust_name


# In[50]:


for i in range(0,len(cust_name)):
    print(cust_name[i])


# # Scrap Reviews

# In[52]:


review=soup.find_all("p",class_="_2-N8zT")
review


# In[54]:


cust_rev=[]

for i in range(0,len(review)):
    cust_rev.append(review[i].get_text())


# In[56]:


cust_rev


# In[58]:


for i in range(0,len(cust_rev)):
    print(cust_rev[i])


# # Scrap Comments

# In[61]:


comment=soup.find_all("div",class_="t-ZTKy")
comment


# In[62]:


cust_comment=[]


for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())


# In[64]:


cust_comment


# In[66]:


for i in range(0,len(cust_comment)):
    print(cust_comment[i])


# # Scrap Rating

# In[67]:


rating=soup.find_all("div",class_="_3LWZlK _1BLPMq")
rating


# In[68]:


cust_rating=[]

for i in range(0,len(rating)):
    cust_rating.append(rating[i].get_text())


# In[70]:


cust_rating


# In[73]:


for i in range(0,len(cust_rating)):
    print(cust_rating[i])


# In[74]:


import pandas as pd


# In[75]:


df=pd.DataFrame()

df["Customer Names"]=cust_name
df["Customer Review"]=cust_rev
df["Customer Comment"]=cust_comment
df["Ratings"]=cust_rating


# In[79]:


df

