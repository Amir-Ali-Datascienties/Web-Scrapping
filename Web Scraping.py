#!/usr/bin/env python
# coding: utf-8

# Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.

# # BeautifulSoup
# 

# Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping

# In[1]:


#!pip install bs4
#!pip install requests


# In[2]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests


# # 1.Write a python program to display all the header tags from wikipedia.org.

# In[3]:


wiki_page = requests.get('https://en.wikipedia.org')


# In[4]:


wiki_page


# In[5]:


wiki_soup = BeautifulSoup(wiki_page.content)
#wiki_soup


# In[6]:


#Scraping Header tags

header_wiki = wiki_soup.find('h1')
header_wiki.text

head_list = ['h1', 'h2', 'h3']
l_head = len(head_list)

for i in range (l_head):
    header_wiki = wiki_soup.find(head_list[i]).text
    print(header_wiki)


# In[7]:


header_wiki = wiki_soup.find('h2')
header_wiki.text


# In[8]:


header_wiki = wiki_soup.find('h3')
header_wiki.text


# # 2.Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[9]:


imdb_page = requests.get('https://www.imdb.com/chart/top/')
imdb_page


# In[10]:


imdb_soup = BeautifulSoup(imdb_page.content)
#imbd_soup


# In[11]:


movies = imdb_soup.find('tbody', class_ = 'lister-list').find_all('tr')
#tbody is tag where al ther related tag available
#in the tbody tag we have tr tage which is use for each different movie attributes.
print(len(movies)) # by printing length of movive tag we can count how  many tr tags or different movies available


# In[12]:


#lest write for loop to itreate each 'tr' tag

for movie in movies:
    movie_name = movie.find('td', class_ = 'titleColumn').a.text# in every 'tr' tag their is 'td' tags where movie name present'
    #in class 'titleColumn' movie title/movie name present.
    rank = movie.find('td', class_ = 'titleColumn').text
    rank = movie.find('td', class_ = 'titleColumn').get_text(strip = True)
    rank = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
    # if we use '.text' it will return all the tags text within 'td' tag
    #strip = true is atribute used to remove all the speacial char and new lines.
    # we can use split function to get rating only, which we done in last rank code line.
    released_year = movie.find('td', class_ = 'titleColumn').span.text.strip('()') #strip '()' to avoid prenthesis
    rating = movie.find('td', class_ = 'ratingColumn imdbRating').get_text(strip = True) #strip = True to avoid special char.
#     print(movie_name)
 #   print(rank)
#     print(rating)
#     print(released_year)
    
#     print(rank,movie_name,released_year, rating)
#     if rank == '100':
#         break


# In[13]:


imdb_movies = []
for movie in movies:
    movie_name = movie.find('td', class_ = 'titleColumn').a.text
    imdb_movies.append(movie_name)
    if len(imdb_movies) == 100:
        break
#print(imdb_movies)


# In[14]:


imdb_rank = []
for movie in movies:
    ranks = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
    imdb_rank.append(ranks)
    if len(imdb_rank) == 100:
        break
#print(imdb_rank)


# In[15]:


imdb_rating = []
for movie in movies:
    rating = movie.find('td', class_ = 'ratingColumn imdbRating').get_text(strip = True)
    imdb_rating.append(rating)
    if len(imdb_rating) == 100:
        break
#print(imdb_rating)


# In[16]:


movie_released = []
for movie in movies:
    released = movie.find('td', class_ = 'titleColumn').span.text
    movie_released.append(released)
    if len(movie_released) == 100:
        break
#movie_released


# In[17]:


import pandas as pd
df = pd.DataFrame({'Imdb Rank':imdb_rank,'Movie Name':imdb_movies,'Released Year':movie_released,'Imdb Ratting':imdb_rating})
df


# # 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[18]:


imdb_hi_page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
imdb_hi_page


# In[19]:


hi_page_soup = BeautifulSoup(imdb_hi_page.content)
#hi_page


# In[20]:


hindi_movies = hi_page_soup.find('tbody', class_ = 'lister-list').find_all('tr')
len(hindi_movies)


# In[21]:


imdb_rank = []

for movie in hindi_movies:
    movies = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
    imdb_rank.append(movies)
    if len(imdb_rank) == 100:
        break
print(imdb_rank)


# In[22]:


imdb_movie = []

for movie in hindi_movies:
    movies = movie.find('td', class_ = "titleColumn").a.text
    imdb_movie.append(movies)
    if len(imdb_movie) == 100:
        break
print(imdb_movie)


# In[23]:


imdb_ratting = []

for movie in hindi_movies:
    movies = movie.find('td', class_ = 'ratingColumn imdbRating').get_text(strip = True)
    imdb_ratting.append(movies)
    if len(imdb_ratting) == 100:
        break
print(imdb_ratting)


# In[24]:


released_year = []

for movie in hindi_movies:
    movies = movie.find('td', class_ = 'titleColumn').span.text.strip("()")
    released_year.append(movies)
    if len(released_year) == 100:
        break
print(released_year)


# In[25]:


df = pd.DataFrame({'Imdb Rank':imdb_rank,'Movie Name':imdb_movie,'Released Year':released_year,'Imdb Ratting':imdb_ratting})
#df


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
# from https://presidentofindia.nic.in/former-presidents.htm

# In[26]:


president = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
#print(president.text[0:])
soup = BeautifulSoup(president.content)
#soup


# Name

# In[27]:


all_president = soup.find_all('div', class_ = "presidentListing")
len(all_president)


# In[28]:


president_name = []
for i in all_president:
    president_name.append(i.get_text(strip = True))
president_name


# Term of office

# In[29]:


term_office = []
for i in all_president:
    term_office.append(i.text.split(":")[1].split("\n")[0])
print(term_office)


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 

# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# 
# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[30]:


cricket_page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
cricket_page


# In[31]:


cricket_soup = BeautifulSoup(cricket_page.content)
#cricket_soup


# In[32]:


all_team = cricket_soup.find('tbody').find_all('tr', class_ = 'table-body')
rank = []

for i in all_team:
    team = i.find('td', class_ = 'table-body__cell table-body__cell--position u-text-right').text
    rank.append(team)

print(rank)

# len(first_team)
# print(first_team)


# In[33]:


team_name = []

for i in all_team:
    team = i.find('td', class_ = "table-body__cell rankings-table__team").find('span', class_ = 'u-hide-phablet').text
    team_name.append(team)
print(team_name)


# In[34]:


matches = []
for i in all_team:
    team = i.find_all('td', class_ = 'table-body__cell u-center-text')[0].text
    matches.append(team)
print(matches)


# In[35]:


points = []
for i in all_team:
    team = i.find_all('td', class_ = 'table-body__cell u-center-text')[1].text
    points.append(team)
print(points)


# In[36]:


ratting = []
for i in all_team:
    team = i.find('td', class_ = 'table-body__cell u-text-right rating').text
    ratting.append(team)
print(ratting)


# In[37]:


df = pd.DataFrame({'Ranks':rank, 'Team Name':team_name, 'Matches':matches, 'Points':points, "Ratting": ratting})
df.iloc[:11,:]


# # b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[38]:


odi_bat = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
odi_bat


# In[39]:


odi_bat_soup = BeautifulSoup(odi_bat.content)
#odi_bat_soup


# In[40]:


all_bat = odi_bat_soup.find('tbody').find_all("tr", class_ = 'table-body')
len(all_bat)


# In[41]:


rank = []

for i in all_bat:
    player = i.find('td', class_ = "table-body__cell table-body__cell--position u-text-right").span.get_text(strip = True)
    rank.append(player)
print(rank)


# In[42]:


Player_name = []
for i in all_bat:
    name = i.find('td', class_ = "table-body__cell name").a.text
    Player_name.append(name)
print(Player_name)


# In[43]:


Nation = []
for i in all_bat:
    country = i.find('td', class_ = 'table-body__cell nationality-logo').find('span', class_ = "table-body__logo-text").text
    Nation.append(country)
print(Nation)


# In[44]:


ratting = []
for i in all_bat:
    rate = i.find('td', class_ = "table-body__cell u-text-right rating").text
    ratting.append(rate)
print(ratting)


# In[45]:


df = pd.DataFrame({'Rank':rank, 'Player Name':Player_name, 'Nation':Nation, 'Ratting':ratting})
df


# # c) Top 10 ODI bowlers along with the records of their team and rating.

# In[46]:


odi_bowlers = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
odi_bowlers


# In[47]:


bowler_soup = BeautifulSoup(odi_bowlers.content)
#bowler_soup


# In[48]:


all_b = bowler_soup.find('tbody').find_all('tr', class_ = 'table-body')
print(len(all_b))


# In[49]:


rank = []

for i in all_b:
    bowl = i.find('div', class_ = 'rankings-table__pos-container').span.get_text(strip = True)
    rank.append(bowl)
print(rank)


# In[50]:


Player_Name = []
for i in all_b:
    player = i.find('td', class_ = "table-body__cell name").a.text
    Player_Name.append(player)
print(Player_Name)


# In[51]:


Nation = []
for i in all_b:
    country = i.find('td', class_ = 'table-body__cell nationality-logo').find('span', class_ = 'table-body__logo-text').text
    Nation.append(country)
print(Nation)


# In[52]:


ratting = []
for i in all_b:
    rate = i.find('td', class_ = 'table-body__cell u-text-right rating').text
    ratting.append(rate)
print(ratting)


# In[53]:


df = pd.DataFrame({'Rank':rank, 'Player Name':Player_name, 'Country':Nation, 'Ratting':ratting})
df


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating

# In[54]:


women_team = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
women_team


# In[55]:


top_team = BeautifulSoup(women_team.content)
#top_team


# In[56]:


all_team = top_team.find('tbody').find_all('tr', class_ = "table-body")
print(len(all_team))


# In[57]:


rank = []
for i in all_team:
    teams = i.find('td', class_ = "table-body__cell table-body__cell--position u-text-right").text
    rank.append(teams)
print(rank)


# In[58]:


team_name = []
for i in all_team:
    teams = i.find('td', class_ = 'table-body__cell rankings-table__team').find('span', class_ = "u-hide-phablet").text
    team_name.append(teams)
print(team_name)


# In[59]:


matches = []
for i in all_team:
    teams = i.find_all('td', class_ ="table-body__cell u-center-text")[0].text
    matches.append(teams)
print(matches)


# In[60]:


points = []
for i in all_team:
    teams = i.find_all('td', class_ = "table-body__cell u-center-text")[1].text
    points.append(teams)
print(points)


# In[61]:


rating = []
for i in all_team:
    teams = i.find('td', class_ = "table-body__cell u-text-right rating").text
    rating.append(teams)
rating


# In[62]:


df = pd.DataFrame({'Rank':rank, "Country": team_name, "Matches":matches, "Points":points, "Ratting":rating})
df


# b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[63]:


batsmen = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
#batsmen


# In[64]:


batswmen_soup = BeautifulSoup(batsmen.content)
#batswmen_soup


# In[65]:


all_w_bat = batswmen_soup.find('table', class_ = 'table rankings-table').find_all('tr', class_ = 'table-body')
len(all_w_bat)


# In[66]:


rank_w = []
for i in all_w_bat:
    team = i.find("td", class_ = "table-body__cell table-body__cell--position u-text-right").get_text(strip = True).split("(")[0]
    rank_w.append(team)
    if len(rank_w) == 10:
        break
print(rank_w)


# In[67]:


player_name_w = []
for i in all_w_bat:
    player = i.find('td', class_ = "table-body__cell rankings-table__name name").a.text
    player_name_w.append(player)
    if len(player_name_w)==10:
        break
print(player_name_w)


# In[68]:


Nation_w = []
for i in all_w_bat:
    country = i.find('td', class_ = "table-body__cell nationality-logo rankings-table__team").get_text(strip = True)
    Nation_w.append(country)
    if len(Nation_w) == 10:
        break
print(Nation_w)


# In[69]:


ratting_w = []
for i in all_w_bat:
    rate = i.find('td', class_ = "table-body__cell rating").text
    ratting_w.append(rate)
    if len(ratting_w)==10:
        break
print(ratting_w)


# In[70]:


df = pd.DataFrame({'Rank': rank_w, "Player Name": player_name_w, "Country":Nation_w, "Ratting":ratting_w})
df


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[71]:


top = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
top


# In[72]:


top_team = BeautifulSoup(top.content)
#top_team


# In[73]:


top_w_allround = top_team.find('table', class_ = "table rankings-table").find_all('tr', class_ = "table-body")
len(top_w_allround)


# In[74]:


rank_al_w = []
for i in top_w_allround:
    rank = i.find('td', class_ = "table-body__cell table-body__cell--position u-text-right").get_text(strip = True).split("(")[0]
    rank_al_w.append(rank)
print(rank_al_w)


# In[75]:


player_al_w = []
for i in top_w_allround:
    player = i.find('td', class_ = "table-body__cell rankings-table__name name").a.text
    player_al_w.append(player)
print(player_al_w)


# In[76]:


nation_al_w = []
for i in top_w_allround:
    country = i.find("td", class_ = "table-body__cell nationality-logo rankings-table__team").get_text(strip = True)
    nation_al_w.append(country)
print(nation_al_w)


# In[77]:


ratting_al_w = []
for i in top_w_allround:
    rate = i.find_all("td", class_ = "table-body__cell rating")[0].text
    ratting_al_w.append(rate)
print(ratting_al_w)


# In[78]:


career_best = []
for i in top_w_allround:
    career = i.find('td', class_ = "table-body__cell u-text-right u-hide-phablet").get_text(strip = True)
    career_best.append(career)
print(career_best)


# In[79]:


df = pd.DataFrame({"Rank": rank_al_w, "Player Name": player_al_w, "Country": nation_al_w, "Ratting":ratting_al_w, "Career Best":career_best})
df.iloc[0:11,:]


# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world

# i) Headline

# In[80]:


cnbc = requests.get("https://www.cnbc.com/world/")
cnbc


# In[81]:


cnbc_soup = BeautifulSoup(cnbc.content)
#cnbc_soup


# In[82]:


Headline = cnbc_soup.find('ul', class_ = "LatestNews-list").find_all("li", class_ = "LatestNews-item")
news = []
for i in Headline:
    latest_news = i.find("div", class_ = "LatestNews-headlineWrapper").a.text
    news.append(latest_news)
print(news)


# ii) Time

# In[83]:


time = []
for i in Headline:
    time_of_news = i.find("div", class_ = "LatestNews-headlineWrapper").find("time", class_ = "LatestNews-timestamp").text
    time.append(time_of_news)
print(time)


# iii) News Link

# In[84]:


new_link = []
# for i in Headline:
#     link = i.find("a", href = True)
# print("Found the URl", i['href'])

for i in cnbc_soup.find_all('a', class_ = "LatestNews-headline", href = True):
    new_link.append(i)
    print("Related URLs", i['href'])


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles

# In[85]:


Ai_articles = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
Ai_articles


# In[86]:


article_soup = BeautifulSoup(Ai_articles.content)
#article_soup


# In[87]:


Articles = article_soup.find("ul", class_ = "sc-9zxyh7-0 cMKaMj").find_all("li", class_ = "sc-9zxyh7-1 sc-9zxyh7-2 kOEIEO hvoVxs")
len(Articles)


# i) Paper Title

# In[88]:


paper_title = []
for i in Articles:
    title = i.find("h2", class_ = "sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg").text
    paper_title.append(title)
print(paper_title)


# i) Authors

# In[89]:


Author = []
for i in Articles:
    auth = i.find("span", class_ = "sc-1w3fpd7-0 dnCnAO").text
    Author.append(auth)
print(Author)


# iii) Published Date 

# In[90]:


publish_d = []
for i in Articles:
    publish = i.find("span", class_ = "sc-1thf9ly-2 dvggWt").text
    publish_d.append(publish)
print(publish_d)


# iv) Paper URL

# In[91]:


url = []
for i in article_soup.find_all("a", class_ ="sc-5smygv-0 fIXTHm", href = True):
    url.append(i)
    print("Related Urls", i['href'])


# # 9) Write a python program to scrape mentioned details from dineout.co.in :

# In[92]:


restaurant = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
restaurant


# In[93]:


rest_soup = BeautifulSoup(restaurant.content)
#rest_soup

all_rest = rest_soup.find("div", class_ ="restnt-card-wrap-new")
len(all_rest)


# i) Restaurant name

# In[94]:


Restaurant_name = []
for i in all_rest:
    rest_name = i.find("div", class_ = "restnt-info cursor").a.text
    Restaurant_name.append(rest_name)
print(Restaurant_name)


# ii) Cuisine

# In[95]:


Cuisine = []
for i in all_rest:
    cuisine_type = i.find("span", class_ = "double-line-ellipsis").a.text
    Cuisine.append(cuisine_type)
print(Cuisine)


# ii) Location 

# In[96]:


Location = []
for i in all_rest:
    loca = i.find("div", class_ = "restnt-loc ellipsis").a.text
    Location.append(loca)
print(Location)


# iv) Ratings

# In[97]:


Ratting = []
for i in all_rest:
    rate = i.find("div", class_ = "restnt-rating rating-4").text
    Ratting.append(rate)
print(Ratting)


# v) Image URL

# In[98]:


image = []
for i in rest_soup.find_all("img", class_ = "no-img"):
    image.append(i.get('data-src'))
image


# # 10) Write a python program to scrape the details of top publications from Google Scholar from 
# https://scholar.google.com/citations?view_op=top_venues&hl=en

# In[99]:


publications = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")
publications


# In[100]:


pub_soup = BeautifulSoup(publications.content)


# i) Rank 

# In[101]:


pub_rank = []
for i in pub_soup.find_all("td", class_ = "gsc_mvt_p"):
    pub_rank.append(i.get_text(strip =True))
print(pub_rank)


# ii) Publication

# In[102]:


public = []
for i in pub_soup.find_all("td", class_ = "gsc_mvt_t"):
    public.append(i.get_text(strip =True))
print(public)


# iii) h5-index

# In[103]:


h5_index = []
for i in pub_soup.find_all("a", class_ = "gs_ibl gsc_mp_anchor"):
    #p = i.find("a",class_ = "gs_ibl gsc_mp_anchor").get_text(strip =True)
    h5_index.append(i.text)
print(h5_index)
# h5_index


# iv) h5-median

# In[104]:


h5_median = []
for i in pub_soup.find_all("td", class_ = "gsc_mvt_n"):
    h5_median.append(i.text)
h5_median


# # Thanks - Amir Ali

# In[ ]:




