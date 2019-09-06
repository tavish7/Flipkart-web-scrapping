#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup

from requests import get
url = 'https://www.flipkart.com/search?q=iphone+x&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_pr&as-pos=1&as-type=RECENT&suggestionId=iphone+x&requestId=cacdf3b6-fdb7-408f-9a3b-1b49e6536d35&as-searchtext=i'
response = get(url)
print(response.text[:1000])

html_soup = BeautifulSoup(response.text,'html.parser')                          #html_soup is the object
type(html_soup)


# In[13]:


phone_containers = html_soup.find_all('div',class_='_1UoZlX')
print(type(phone_containers))
print(len(phone_containers))


# In[15]:


phone_containers[0]
first_phone= phone_containers[0]
phone_name= first_phone.find('div', class_='_3wU53n' )
phone_name=phone_name.text
print(phone_name)


# In[6]:


phone_cost = first_phone.find('div', class_='_1vC4OE _2rQ-NK' )
phone_cost=phone_cost.text
print(phone_cost)


# In[7]:


phone_rating = first_phone.find('div', class_='hGSR34' )
phone_rating=phone_rating.text
print(phone_rating)


# In[8]:


names= []
costs= []
ratings=[]

for container in phone_containers:
    name=container.find('div', class_='_3wU53n' ).text
    names.append(name)
    cost=container.find('div', class_='_1vC4OE _2rQ-NK' ).text
    costs.append(cost)
    #rating=container.find('div',class_='hGSR34' )
    #ratings.append(rating)


# In[9]:


names


# In[10]:


costs


# In[11]:


import pandas as pd
test_df = pd.DataFrame({'Model':names,
                        'Price':costs,})                                             #DataFrame has D and F capitals


print(test_df.info())
test_df


# In[12]:


filename = "product.csv"
f = open(filename,"w")
headers = "Product_Name,Price,Rating\n"
f.write(headers)

for container in phone_containers:
    name=container.find('div', class_='_3wU53n' ).text
    cost=container.find('div', class_='_1vC4OE _2rQ-NK' ).text
        
    print("product_name:" + name)
    print("price:" + cost)
    

