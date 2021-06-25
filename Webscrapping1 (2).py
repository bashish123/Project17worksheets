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
headings=soup.find_all('span',class_="mw-headline")


# In[6]:


#collect all headings in list
heading_list=[]
for i in headings:
    heading_list.append(i.text)
heading_list


# #### 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame

# In[7]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[8]:


content=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
soup=BeautifulSoup(content.text)
mix=soup.find_all('td',class_="titleColumn")
mix1=[]
j=0
for i in mix:
    if j>99:
        break
    else:
        mix1.append(i.text.replace('\n',''))
    j+=1


# In[9]:


Year=[]
for i in mix1:
    Year.append(i[-5:-1:].strip())
name=[]
for i in mix1:
    name.append(i[:-6:])
rating=soup.find_all('td',class_='ratingColumn imdbRating')
rstg=[]
j=0
for i in rating:
    if j>99:
        break
    else:
        rstg.append(i.text.replace('\n',''))
    j+=1


# In[10]:


df=pd.DataFrame()
df['Movie Name']=name
df['Year']=Year
df['Rating']=rstg
df


# #### 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame.

# In[11]:


content=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2e9dfa9b-3e4d-4d39-acd2-8af11f252a59&pf_rd_r=JF1X5WCBEWDS4FFYY20Y&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_india_tr_rhs_1")
soup=BeautifulSoup(content.text)
mix=soup.find_all('td',class_="titleColumn")
mix1=[]
j=0
for i in mix:
    if j>99:
        break
    else:
        mix1.append(i.text.replace('\n',''))
    j+=1


# In[12]:


Year=[]
for i in mix1:
    Year.append(i[-5:-1:].strip())
name=[]
for i in mix1:
    name.append(i[:-6:])
rating=soup.find_all('td',class_='ratingColumn imdbRating')
rstg=[]
j=0
for i in rating:
    if j>99:
        break
    else:
        rstg.append(i.text.replace('\n',''))
    j+=1


# In[13]:


df=pd.DataFrame()
df['Movie Name']=name
df['Year']=Year
df['Rating']=rstg
df


# #### 4. Write a python program to scrap book name, author name, genre and book review of any 5 books from
# ‘www.bookpage.com’

# In[14]:


page=requests.get("https://bookpage.com/reviews?book_genre=fiction&page=1")
page


# In[15]:


soup=BeautifulSoup(page.content)
#soup


# In[16]:


Book_title=soup.find_all('h4',class_="italic")
#Book_title


# In[17]:


Book_Name=[]
for j in Book_title:
    Book_Name.append(j.text.replace('\n',''))


# In[18]:


Book_Name


# In[19]:


Book_author=soup.find_all('p',class_="sans bold")


# In[20]:


Author_Name=[]
for i in Book_author:
    Author_Name.append(i.text.replace('\n',''))


# In[21]:


Author_Name


# In[22]:


Excerpt=soup.find_all('p',class_="excerpt")


# In[23]:


Excerpt_B=[]
for i in Excerpt:
    Excerpt_B.append(i.text.replace('\n',''))


# In[24]:


print(len(Book_Name),len(Author_Name),len(Excerpt_B))


# In[25]:


store=pd.DataFrame()
store['Book Name']=Book_Name
store['Author_Name']=Author_Name
store['Excerpt_B']=Excerpt_B


# In[26]:


store


# #### 5. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
# iii) Top 10 ODI bowlers along with the records of their team and rating.

# ##### i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[27]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[28]:


soup=BeautifulSoup(page.content)
Team_name1=soup.find_all('span',class_='u-hide-phablet')


# In[29]:


Team_name=[]
j=0
for i in Team_name1:
        Team_name.append(i.text)
        j+=1
        if j>9:
            break


# In[30]:


Team_matches1=soup.find_all('td',class_="rankings-block__banner--matches")
Team_matches=[]
for i in Team_matches1:
    Team_matches.append(i.text)


# In[31]:


Team_points1=soup.find_all('td',class_="rankings-block__banner--points")
Team_points=[]
for i in Team_points1:
    Team_points.append(i.text)


# In[32]:


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


# In[33]:


Team_Rating1=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
Team_Rating=[]
for i in Team_Rating1:
    Team_Rating.append(i.text.replace('\n','').replace(' ',''))


# In[34]:


Team_Rating1=soup.find_all('td',class_="table-body__cell u-text-right rating")


# In[35]:


j=0
for i in Team_Rating1:
    if j<9:
        Team_Rating.append(i.text.replace('\n',''))
    else:
        break
    j+=1


# In[36]:


cricket=pd.DataFrame()
cricket['Team Name']=Team_name
cricket['Team Matches']=Team_matches
cricket['Team Point']=Team_points
cricket['Team Rating']=Team_Rating


# In[37]:


print("="*32,'ODI Men Teams',"="*32)
cricket


# ##### ii) Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[38]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[39]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page
soup=BeautifulSoup(page.content)


# In[40]:


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


# In[41]:


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


# In[42]:


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


# In[43]:


Batsman=pd.DataFrame()
Batsman['Player']=Pl
Batsman['Team']=Team
Batsman['Rating']=Rating
print("="*32,'Batsman',"="*32)
print("="*32,'       ',"="*32)
Batsman


# ##### iii) Top 10 ODI bowlers along with the records of their team and rating.

# In[44]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page
soup=BeautifulSoup(page.content)


# In[45]:


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


# In[46]:


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


# In[47]:


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


# In[48]:


print("="*32,'BOWLERS',"="*32)
bowlers=pd.DataFrame()
bowlers['Player']=Ply
bowlers['Team']=Team
bowlers['Rating']=Rating
bowlers


# #### 6. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape: Women

# In[49]:


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


# In[50]:


Team_matches1=soup.find_all('td',class_="rankings-block__banner--matches")
Team_matches=[]
for i in Team_matches1:
    Team_matches.append(i.text)


# In[51]:


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


# In[52]:


Team_Rating1=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
Team_Rating=[]
for i in Team_Rating1:
    Team_Rating.append(i.text.replace('\n','').replace(' ',''))
Team_Rating1=soup.find_all('td',class_="table-body__cell u-text-right rating")
for i in Team_Rating1:
        Team_Rating.append(i.text.replace('\n',''))


# In[53]:


cricket=pd.DataFrame()
cricket['Team Name']=Team_name
cricket['Team Matches']=Team_matches
cricket['Team Point']=Team_points
cricket['Team Rating']=Team_Rating
print("="*32,'ODI Women Teams',"="*32)
cricket


# #### ii) Top 10 women’s ODI players along with the records of their team and rating.

# In[54]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page
soup=BeautifulSoup(page.content)


# In[55]:


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


# In[56]:


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


# In[57]:


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


# In[58]:


Batsman=pd.DataFrame()
Batsman['Player']=Pl
Batsman['Team']=Team
Batsman['Rating']=Rating
print("="*32,'Batting',"="*32)
print("="*32,'       ',"="*32)
Batsman


# #### iii) Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[59]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[60]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page
soup=BeautifulSoup(page.content)


# In[61]:


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


# In[62]:


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


# In[63]:


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


# In[64]:


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


# In[65]:


WAR=pd.DataFrame()
WAR['Team']=Team
WAR['Player']=Pl
WAR['Rating']=Rating
WAR['Carrier Best Rating']=CBR
print("="*32,'ODI Women Teams',"="*32)
WAR


# ### 9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title,company name, CTC, and apply date.

# In[66]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[67]:


JT=[]
CN=[]
for i in range(1,4,1):
    page=requests.get("https://internshala.com/fresher-jobs/page"+'-'+str(i))
    soup=BeautifulSoup(page.content)
    JT1=soup.find_all('div',class_='heading_4_5 profile')
    CN1=soup.find_all('div',class_='heading_6 company_name')
    for j in JT1:
            JT.append(j.text.replace('\n','').replace(' ',''))
    for c in CN1:
            CN.append(c.text.replace('\n','').replace(' ',''))


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


# In[69]:


apply_date=[]
for i in CTC:
    if i[-1::]!='A':
        apply_date.append(i)
        CTC.remove(i)        


# In[70]:


len(apply_date),len(CTC),len(JT)


# In[71]:


CN=[]
for i in range(1,4,1):
    page=requests.get("https://internshala.com/fresher-jobs/page"+'-'+str(i))
    soup=BeautifulSoup(page.content)
    CN1=soup.find_all('div',class_='heading_6 company_name')
    for i in CN1:
        CN.append(i.text.replace('\n','').replace(' ',''))
len(CN)        


# In[72]:


int_shal=pd.DataFrame()
int_shal['Company Name']=CN
int_shal['Job Title']=JT
int_shal['CTC']=CTC
int_shal['Apply Date']=apply_date


# In[73]:


int_shal


# 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of
# release) and make data frame.
# 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year
# of release) and make data frame.


# 7. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The
# scraped data should include Product Name, Price, Image URL and Average Rating.


# 10. Write a python program to scrape house details from mentioned url. It should include house title, location,
# area, emi and price
https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N
DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8
iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0"
# ### 8. Write a python program to extract information about the local weather from the National Weather Servicewebsite of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day extended forecast display for the city. The data should include period, short description, temperature and description.

# In[92]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[93]:


page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196")
soup=BeautifulSoup(page.content)


# In[94]:


pr=soup.find_all('p',class_='period-name')
Period=[]
for i in pr:
    Period.append(i.text)


# In[95]:


sd=soup.find_all('p',class_='short-desc')
SD=[]
for i in sd:
    SD.append(i.text)


# In[96]:


TP=[]
tph=soup.find_all('p',class_='temp temp-high')
tpl=soup.find_all('p',class_='temp temp-low')
k=0
for j in tph:
    TP.append(j.text.replace('\n',''))
    if k==4:
        break        
    TP.append(tpl[k].text.replace('\n',''))
    k+=1
dis1=[]
j=0
discrp=soup.find_all('div',class_="col-sm-10 forecast-text")
for i in discrp:
    if j<9:
        dis1.append(i.text)
    else:
        break
    j+=1


# In[97]:


len(pr),len(SD),len(TP),len(dis1)


# In[98]:


df=pd.DataFrame()
df['Period']=pr
df['Short Desc.']=SD
df['Temp.']=TP
df['Discreption']=dis1
df


# ### 10. Write a python program to scrape house details from mentioned url. It should include house title, location,area, emi and price
# 

# In[63]:


#importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[64]:


page=requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?type=BHK4&searchParam=W3sibGF0IjoxMi45MTM5MDk2LCJsb24iOjc3LjYxMDE2OTEsInBsYWNlSWQiOiJDaElKTDRqNUFfMFVyanNSNHhmb3R6ejc4ckkiLCJwbGFjZU5hbWUiOiJIb3RlbCBTd2FkaXNodGEgQWFoYXIifSx7ImxhdCI6MTIuOTczMDM4LCJsb24iOjc3LjU3ODIxMzIsInBsYWNlSWQiOiJDaElKMzVHWXV3NFdyanNSMlc5b0xvQ3BhZWciLCJwbGFjZU5hbWUiOiJIb3NwaXRhbCBSb2FkIn0seyJsYXQiOjEyLjg3NjEyODcsImxvbiI6NzcuNjEyMTcwNDAwMDAwMDEsInBsYWNlSWQiOiJDaElKSjN6bGFpdHJyanNSbzh6a3p5NU43emciLCJwbGFjZU5hbWUiOiJIb3VzZSBvZiBIaXJhbmFuZGFuaSBMYWtlIFZlcmFuZGFocyJ9XQ==&propertyAge=0&radius=2.0")
soup=BeautifulSoup(page.content)


# In[67]:


ht=[]
ht1=soup.find_all('h2',class_="heading-6 font-semi-bold nb__1AShY")
for i in ht1:
    ht.append(i.text)


# In[68]:


lo=[]
loc=soup.find_all('div',class_="nb__2CMjv")
for i in loc:
    lo.append(i.text)


# In[69]:


ar=[]
area=soup.find_all('div',class_="nb__3oNyC")
for i in area:
    ar.append(i.text)


# In[70]:


em=[]
em2=[]
price=[]
emi=soup.find_all('div',class_="nb__2NPHR")
j=2
while j<40:
    em.append(emi[j].text)
    price.append(emi[j+1].text)
    j+=4
for i in em:
    em2.append(i[:-13:])


# In[71]:


df=pd.DataFrame()
df['House Title']=ht
df['Location']=lo
df['Area']=ar
df['Price']=price
df['EMI']=em2
df


# ### 7. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The scraped data should include Product Name, Price, Image URL and Average Rating.

# In[ ]:




