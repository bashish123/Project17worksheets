#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# 

# In[2]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page=requests.get("http://en.wikipedia.org/wiki/Main_Page?")
page


# In[4]:


soup=BeautifulSoup(page.content)


# #### 1. Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.

# In[5]:


first_title=soup.find('span',class_="mw-headline")
first_title


# In[6]:


first_title.text


# In[7]:


headings=soup.find_all('span',class_="mw-headline")


# In[8]:


for i in headings:
    print(i.text)


# In[9]:


#collect all headings in list
heading_list=[]
for i in headings:
    heading_list.append(i.text)
heading_list


# #### 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame

# In[10]:


content=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")


# In[11]:


soup=BeautifulSoup(content.text,'html.parser')


# #### 4. Write a python program to scrap book name, author name, genre and book review of any 5 books from
# ‘www.bookpage.com’

# In[12]:


page=requests.get("https://bookpage.com/reviews?book_genre=fiction&page=1")
page


# In[13]:


#page.content


# In[14]:


soup=BeautifulSoup(page.content)
#soup


# In[15]:


Book_title=soup.find_all('h4',class_="italic")
#Book_title


# In[16]:


Book_Name=[]
for j in Book_title:
    Book_Name.append(j.text.replace('\n',''))


# In[17]:


Book_Name


# In[18]:


Book_author=soup.find_all('p',class_="sans bold")


# In[19]:


Author_Name=[]
for i in Book_author:
    Author_Name.append(i.text.replace('\n',''))


# In[20]:


Author_Name


# In[21]:


Excerpt=soup.find_all('p',class_="excerpt")


# In[22]:


Excerpt_B=[]
for i in Excerpt:
    Excerpt_B.append(i.text.replace('\n',''))


# In[23]:


print(len(Book_Name),len(Author_Name),len(Excerpt_B))


# In[24]:


store=pd.DataFrame()
store['Book Name']=Book_Name
store['Author_Name']=Author_Name
store['Excerpt_B']=Excerpt_B


# In[25]:


store


# #### 5. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
# iii) Top 10 ODI bowlers along with the records of their team and rating.

# ##### i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[152]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[153]:


soup=BeautifulSoup(page.content)
Team_name1=soup.find_all('span',class_='u-hide-phablet')


# In[154]:


Team_name=[]
j=0
for i in Team_name1:
        Team_name.append(i.text)
        j+=1
        if j>9:
            break


# In[155]:


Team_matches1=soup.find_all('td',class_="rankings-block__banner--matches")
Team_matches=[]
for i in Team_matches1:
    Team_matches.append(i.text)


# In[156]:


Team_points1=soup.find_all('td',class_="rankings-block__banner--points")
Team_points=[]
for i in Team_points1:
    Team_points.append(i.text)


# In[157]:


Team_m_and_p1=soup.find_all('td',class_="table-body__cell u-center-text")
j==2
for i in Team_m_and_p1:
    if j%2==0:
        if j>26:
            continue
        else:
            Team_matches.append(i.text)            
    else:
        if j>36:
            continue
        else:
            Team_points.append(i.text)            
    j+=1


# In[158]:


Team_Rating1=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
Team_Rating=[]
for i in Team_Rating1:
    Team_Rating.append(i.text.replace('\n','').replace(' ',''))


# In[159]:


Team_Rating1=soup.find_all('td',class_="table-body__cell u-text-right rating")


# In[160]:


j=0
for i in Team_Rating1:
    if j<9:
        Team_Rating.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[161]:


cricket=pd.DataFrame()
cricket['Team Name']=Team_name
cricket['Team Matches']=Team_matches
cricket['Team Point']=Team_points
cricket['Team Rating']=Team_Rating


# In[162]:


print("="*32,'ODI Men Teams',"="*32)
cricket


# ##### ii) Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[89]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[90]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page
soup=BeautifulSoup(page.content)


# In[91]:


Pl=[]
Batsman1=soup.find_all('div',class_='rankings-block__banner--name-large')
for i in Batsman1:
    Pl.append(i.text)
Batsman1=soup.find_all('td',class_='table-body__cell rankings-table__name name')
j=0
for i in Batsman1:
    if j<9:
        Pl.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[92]:


Team1=soup.find_all('div',class_='rankings-block__banner--nationality')
Team=[]
for i in Team1:
    Team.append(i.text.replace('\n',''))
Team1=soup.find_all('span',class_='table-body__logo-text')
j=0
for i in Team1:
    if j<9:
        Team.append(i.text)
    else:
        break
    j+=1


# In[94]:


Rating1=soup.find_all('div',class_="rankings-block__banner--rating")
Rating=[]
for i in Rating1:
    Rating.append(i.text)
Rating1=soup.find_all('td',class_="table-body__cell rating")
j=0
for i in Rating1:
    if j<9:
        Rating.append(i.text)
    else:
        break
    j+=1


# In[98]:


Batsman=pd.DataFrame()
Batsman['Player']=Pl
Batsman['Team']=Team
Batsman['Rating']=Rating
print("="*32,'Batsman',"="*32)
print("="*32,'       ',"="*32)
Batsman


# ##### iii) Top 10 ODI bowlers along with the records of their team and rating.

# In[46]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page
soup=BeautifulSoup(page.content)


# In[47]:


Ply=[]
Bowler1=soup.find_all('div',class_='rankings-block__banner--name-large')
for i in Bowler1:
    Ply.append(i.text)
Bowler1=soup.find_all('td',class_='table-body__cell rankings-table__name name')
j=0
for i in Bowler1:
    if j<9:
        Ply.append(i.text.replace('\n',''))
    else:
        break
    j+=1    


# In[48]:


Team1=soup.find_all('div',class_='rankings-block__banner--nationality')
Team=[]
for i in Team1:
    Team.append(i.text.replace('\n',''))
Team1=soup.find_all('span',class_='table-body__logo-text')
j=0
for i in Team1:
    if j<9:
        Team.append(i.text)
    else:
        break
    j+=1


# In[49]:


Rating1=soup.find_all('div',class_="rankings-block__banner--rating")
Rating=[]
for i in Rating1:
    Rating.append(i.text)
Rating1=soup.find_all('td',class_="table-body__cell rating")
j=0
for i in Rating1:
    if j<9:
        Rating.append(i.text)
    else:
        break
    j+=1
Rating


# In[50]:


print("="*32,'BOWLERS',"="*32)
bowlers=pd.DataFrame()
bowlers['Player']=Ply
bowlers['Team']=Team
bowlers['Rating']=Rating
bowlers


# ### Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:

# In[146]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
soup=BeautifulSoup(page.content)
Team_name1=soup.find_all('span',class_='u-hide-phablet')
Team_name=[]
j=0
for i in Team_name1:
        Team_name.append(i.text)
        j+=1
        if j>9:
            break 


# In[147]:


Team_matches1=soup.find_all('td',class_="rankings-block__banner--matches")
Team_matches=[]
for i in Team_matches1:
    Team_matches.append(i.text)


# In[148]:


Team_points1=soup.find_all('td',class_="rankings-block__banner--points")
Team_points=[]
for i in Team_points1:
    Team_points.append(i.text)
Team_m_and_p1=soup.find_all('td',class_="table-body__cell u-center-text")
j==2
for i in Team_m_and_p1:
    if j%2==0:
        if j>30:
            continue
        else:
            Team_matches.append(i.text)            
    else:
        if j>31:
            continue
        else:
            Team_points.append(i.text)            
    j+=1


# In[149]:


Team_Rating1=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
Team_Rating=[]
for i in Team_Rating1:
    Team_Rating.append(i.text.replace('\n','').replace(' ',''))
Team_Rating1=soup.find_all('td',class_="table-body__cell u-text-right rating")
for i in Team_Rating1:
        Team_Rating.append(i.text.replace('\n',''))


# In[150]:


cricket=pd.DataFrame()
cricket['Team Name']=Team_name
cricket['Team Matches']=Team_matches
cricket['Team Point']=Team_points
cricket['Team Rating']=Team_Rating
print("="*32,'ODI Women Teams',"="*32)
cricket


# #### ii) Top 10 women’s ODI players along with the records of their team and rating.

# In[14]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page
soup=BeautifulSoup(page.content)


# In[15]:


Pl=[]
Batting1=soup.find_all('div',class_='rankings-block__banner--name-large')
for i in Batting1:
    Pl.append(i.text)
Batting1=soup.find_all('td',class_='table-body__cell rankings-table__name name')
j=0
for i in Batting1:
    if j<9:
        Pl.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[16]:


Team1=soup.find_all('div',class_='rankings-block__banner--nationality')
Team=[]
for i in Team1:
    Team.append(i.text.replace('\n',''))
Team1=soup.find_all('span',class_='table-body__logo-text')
j=0
for i in Team1:
    if j<9:
        Team.append(i.text)
    else:
        break
    j+=1


# In[18]:


Rating1=soup.find_all('span',class_="rankings-block__career-best-text")
Rating=[]
for i in Rating1:
    Rating.append(i.text.replace('\n',''))
Rating1=soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet")
j=0
for i in Rating1:
    if j<9:
        Rating.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[19]:


Batsman=pd.DataFrame()
Batsman['Player']=Pl
Batsman['Team']=Team
Batsman['Rating']=Rating
print("="*32,'Batting',"="*32)
print("="*32,'       ',"="*32)
Batsman


# #### iii) Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[139]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[140]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page
soup=BeautifulSoup(page.content)


# In[141]:


Team=[]
Team1=soup.find_all('div',class_='rankings-block__banner--nationality')
for i in Team1:
    Team.append(i.text.replace('\n',''))
Team
Team1=soup.find_all('span',class_='table-body__logo-text')
j=0
for i in Team1:
    if j<9:
        Team.append(i.text)
    else:
        break
    j+=1


# In[142]:


Pl=[]
Name1=soup.find_all('div',class_='rankings-block__banner--name-large')
for i in Name1:
    Pl.append(i.text)
Name1=soup.find_all('td',class_='table-body__cell rankings-table__name name')
j=0
for i in Name1:
    if j<9:
        Pl.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[143]:


Rating1=soup.find_all('div',class_="rankings-block__banner--rating")
Rating=[]
for i in Rating1:
    Rating.append(i.text.replace('\n',''))
Rating1=soup.find_all('td',class_="table-body__cell rating")
j=0
for i in Rating1:
    if j<9:
        Rating.append(i.text.replace('\n',''))
    else:
        break
    j+=1
Rating


# In[144]:


CBR1=soup.find_all('span',class_="rankings-block__career-best-text")
CBR=[]
for i in CBR1:
    CBR.append(i.text.replace('\n',''))
CBR1=soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet")
j=0
for i in CBR1:
    if j<9:
        CBR.append(i.text.replace('\n','').replace(' ',''))
    else:
        break
    j+=1


# In[145]:


WAR=pd.DataFrame()
WAR['Team']=Team
WAR['Player']=Pl
WAR['Rating']=Rating
WAR['Carrier Best Rating']=CBR
print("="*32,'ODI Women Teams',"="*32)
WAR


# ### 9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title,company name, CTC, and apply date.

# In[26]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import io


# In[36]:


JT=[]
CN=[]
for i in range(1,4,1):
    page=requests.get("https://internshala.com/fresher-jobs/page"+'-'+str(i))
    soup=BeautifulSoup(page.content)
    JT1=soup.find_all('div',class_='heading_4_5 profile')
    CN1=soup.find_all('div',class_='heading_6 company_name')
    for i in JT1 and CN1:
            JT.append(i.text.replace('\n','').replace(' ',''))
            CN.append(i.text.replace('\n','').replace(' ',''))


# In[38]:


len(CN)


# In[68]:


CTC=[]
for i in range(1,4,1):
    page=requests.get("https://internshala.com/fresher-jobs/page"+'-'+str(i))
    soup=BeautifulSoup(page.content)
    CTC1=soup.find_all('div',class_='item_body')
    for i in CTC1:
            CTC.append(i.text.replace('\n','').replace(' ',''))
    for i in CTC:
        if i=='Starts\xa0Immediately':
            CTC.remove(i)
        else:
            pass


# In[71]:


CTC


# In[75]:


apply_date=[]
j=2
for i in CTC:
    if j%2==0:
        pass
    else:
        CTC.remove(i) and apply_date.append(i)


# In[76]:


CTC


# In[ ]:


# 1. Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.
# 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of
# release) and make data frame.
# 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year
# of release) and make data frame.
# 4. Write a python program to scrap book name, author name, genre and book review of any 5 books from
# ‘www.bookpage.com’
# 5. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
# iii) Top 10 ODI bowlers along with the records of their team and rating.
# 6. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# ii) Top 10 women’s ODI players along with the records of their team and rating.
# iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 7. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The
# scraped data should include Product Name, Price, Image URL and Average Rating.
# 8. Write a python program to extract information about the local weather from the National Weather Service
# website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day
# extended forecast display for the city. The data should include period, short description, temperature and
# description.
# 9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title,
# company name, CTC, and apply date.
# 10. Write a python program to scrape house details from mentioned url. It should include house title, location,
# area, emi and price
# https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N
# DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8
# iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0"

