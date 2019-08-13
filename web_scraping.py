import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

# task 1  
url = "https://www.imdb.com/india/top-rated-indian-movies/"
# print (url)
def scrap_to_tist():
    sample = requests.get(url)
    # print(sample)
    soup = BeautifulSoup(sample.text,"html.parser") 
    # print (soup)
    tbody = soup.find("tbody",class_="lister-list")
    # print (tboday)
    trs = tbody.findAll("tr")
    # print (trs)
    movie_list = []
    j = 0
    for i in trs:
        new = {}
        position = j = j + 1
        # print(position)
        name = i.find("td",class_ = "titleColumn").a.get_text()
        # print(name)
        year = i.find("td",class_ = "titleColumn").span.get_text()
        # print (year)
        reng = i.find("td",class_ = "ratingColumn").get_text()
        # print (reng)
        link = i.find("a")
        movie_link = "https://www.imdb.com/"+link["href"]
        # print (movie_link)
        new["position"] = position
        new["name"] = name
        new["year"] = int(year[1:5])
        new["reting"] = float(reng)
        new["url"] = movie_link
        movie_list.append(new)
        with open("movie_data.json","w") as fs:
            (json.dump(movie_list,fs,indent = 1))
    return movie_list
scrept = scrap_to_tist()
# pprint (scrept) 

# task 2

def group_by_year(movies):
    # print(movies)
    year = []
    movie_dict = {}
    for i in movies:
        # print (i)
        # print (movies)
        years = i["year"]
        # print(years)
        if years not in year:
            # print(years)
            # print (year)
            year.append(years)
            # print(year)
    # movie_dict = {i:[] for i in year}
    for i in year:
        movie_dict[i] = []
    for i in movies:
        # print (i)
        # print (movies)
        year_1 = i["year"]
        # print (year_1)
        for x in movie_dict:
            # print(x)
            # print(movie_dict)
            if x == year_1:
                # print (x)
                # print(year)
                movie_dict[x].append(i)
                # print (movie_dict)
                # print(movie_dict[x])
    return movie_dict
dec_arg = group_by_year(scrept)
# pprint (dec_arg)

# task 3 

def group_by_decade(movies):
    moviedec = {}
    list1 = []
    for index in movies:
        # print (movies)
        # print(index)
        mod = index % 10
        # print(mod)
        decade = index - mod
        # print(decade)
        if decade not in list1:
            # print(decade)
            list1.append(decade)
        # print(list1)
    list1.sort()
    # print(list1)
    for i in list1:
        # print(i)
        # print(list1)
        moviedec[i] = []
        # print(moviedec)
    for i in moviedec:
        # print(j)
        # print(moviedec)
        dec10 = i + 9
            # print (dec10)
        for x in movies:
            # print (x)
            if x <= dec10 and x >= i:
                # print (dec10)
                # print (x)
                # print (i)
                for v in movies[x]:
                    # print(v)
                    moviedec[i].append(v)
    return (moviedec)    
movie_group = group_by_decade(dec_arg)
# pprint(movie_group)

# task 4 

def scrap_movie_details(movie_url):
    page = requests.get(movie_url)
    # print (page)
    soup = BeautifulSoup(page.text,"html.parser") 
    # print (soup)
    name_div = soup.find("div", class_ = "title_bar_wrapper").h1.get_text().split()[0]
    # print (name_div)
    sub_div = soup.find("div", class_="subtext")
    # print (sub_div)
    runtime = sub_div.find("time").get_text().strip()
    # print(runtime)
    runtime_hours = int(runtime[0])*60
    # print(runtime_hours)
    movie_poster_list = soup.find("div", class_="poster").a["href"]
    # print (poster_image_list)
    movie_poster = "https://www.imdb.com" + movie_poster_list
    # print (movie_poster)
    movie_bio = soup.find("div", class_= "summary_text").get_text().strip()
    # print (movie_bio)
    movie_director = soup.find("div", class_="credit_summary_item").get_text().strip()
    # print(movie_director)
    director = movie_director[9:].strip()
    # print(director)
    movie_genre = soup.find("div", class_="subtext").a.get_text()
    # print(movie_genre)
    extra_details = soup.find("div",class_="article",id ="titleDetails")
    # print(extra_details)
    list_of_divs = extra_details.findAll("div")
    # print (list_of_divs)
    for div in list_of_divs:
        tag_h4 = div.findAll("h4")
        # print (tag_h4)
        for text in tag_h4:
            if "Language:" in text:
                # print (text)
                tag_anchor = div.findAll("a")
                # print (tag_anchor)
                for language in tag_anchor:
                    movie_language = [language.get_text()]
                    # print (movie_language)
            elif "Country:" in text:
                # print (text)
                tag_anchor = div.findAll("a")
                # print (tag_anchor)
                for Country in tag_anchor:
                    movie_Country = [Country.get_text()]
                    # print (movie_Country)
    movie_detail_div = {"name": "","director":"","bio":"","runtime":"","gener":"","language":"","country":"","poster_img_url":""}
    
    movie_detail_div["name"] = name_div
    movie_detail_div["director"] = director
    movie_detail_div["bio"] = movie_bio
    movie_detail_div["runtime"] = runtime_hours
    movie_detail_div["gener"] = movie_genre
    movie_detail_div["language"] = movie_language
    movie_detail_div["country"] = movie_Country
    movie_detail_div["poster_img_url"] = movie_poster

    return movie_detail_div
url1 = scrept[88]["url"]
movie_detail = scrap_movie_details(url1)
pprint (movie_detail)
