import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from pathlib import Path
import random
# help(random.randint)
import time
# help(time.sleep)

# task 1 
URL = "https://www.imdb.com/india/top-rated-indian-movies/" 
def scrap_to_tist():
        sample = requests.get(URL)
        soup = BeautifulSoup(sample.text,"html.parser") 
        # print (soup)
        tbody = soup.find("tbody",class_ = "lister-list")
        trs = tbody.findAll('tr')
        # print (trs)
        movie_list = []
        j = 0
        for i in trs :
                new = {}
                position = j = j + 1
        
                name = i.find("td",class_ = "titleColumn").a.get_text()
                # print (name)
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
                with open("data.json","w") as fs:
                        json.dump(movie_list,fs,indent = 1 )

        return movie_list

scrept = scrap_to_tist()
# pprint (scrept) 


# task 2
def group_by_year(movies):
        years = []
        for i in movies:
                year = i["year"]
                if year not in years:
                        years.append(year)
        movie_dict = {i:[]for i in years}
        for i in movies:
                year = i["year"]
                for x in movie_dict:
                        if str(x) == str(year):
                                movie_dict[x].append(i)
        return movie_dict
dec_arg = group_by_year(scrept)
# pprint (dec_arg)



# task 3
def group_by_decade(movies):
        moviedec = {}
        list1 = []
        for index in movies:
                # print (movies)
                mod = index % 10
                decade = index - mod
                if decade not in list1:
                        list1.append(decade)
        list1.sort()

        for i in list1:
                moviedec[i] = []
        for i in moviedec:
                # print (i)
                dec10 = i + 9
                # print (dec10)
                for x in movies:
                        # print (x)
                        # print (movies)
                        if x <= dec10 and x >= i:
                                # print (dec10)
                                # print (x)
                                # print (i)
                                for v in movies[x]:
                                        moviedec[i].append(v)
        return (moviedec)
movie_group = group_by_decade(dec_arg)
# pprint (movie_group)


# task 4
def scrap_movie_details(movie_url):
        # print (movie_url)
        # task 9
        random_sleep = random.randint(1,3)
        # print (random_sleep)
        Id = movie_url.split("/")
        # print (Id)
        file_name_id = Id[5]
        # print (file_name_id)

        # task 8
        file_name="caching8/"+file_name_id + ".json"
        filepath=Path(file_name)
        if filepath.exists():
                with open(file_name, "r") as file1:
                        top_movies_read = file1.read()
                        movies_lode = json.loads(top_movies_read)
                        print ("file exists")
                return movies_lode

        else:
                print ("file not exsits")
                movies_data_scrape = {}
                # task 9Rashmi
                time.sleep(random_sleep)
                # task 4
                page = requests.get(movie_url)
                # print page
                soup = BeautifulSoup(page.text,"html.parser") 
                # print (soup)

                title_div = soup.find("div", class_ = "title_bar_wrapper").h1.get_text().split('(')
                # print (title_div)
                movie_name = title_div[0]
                # print (movie_name)
                
                sub_div = soup.find("div", class_ = "subtext")
                # print (sub_div)
                runtime = sub_div.find("time").get_text().strip()
                # print (runtime)
                runtime_hours = int(runtime[0])*60
                # print (runtime_hours)
                if "min" in sub_div:
                        # print (sub_div)
                        # print (["min"])
                        runtime_minutes = int(movie_runtime[3:].strip("min"))
                        # print (movie_runtime)
                        # print (runtime_minutes)
                        movie_runtime = runtime_hours + runtime_minutes
                        # print (movie_runtime)
                else:
                        movie_runtime = runtime_hours
                        # print (movie_runtime)
                gener = sub_div.find_all("a")
                # print (gener)
                gener.pop()
                # print (gener)
                movie_group = [i.get_text()for i in gener]
                # print (movie_group)
                sumary = soup.find("div", class_= "plot_summary")
                # print (sumary)
                movie_bio = sumary.find("div", class_= "summary_text").get_text().strip()
                # print (movie_bio)
                director = sumary.find("div", class_= "credit_summary_item")
                # print (director)
                director_list = director.find_all("a")
                # print (director_list)
                movie_directors = [i.get_text().strip() for i in director_list]
                # print (movie_directors)
                extra_details = soup.find("div", attrs = {"class":"article","id":"titleDetails"})
                # print (extra_details)
                list_of_divs = extra_details.find_all("div")
                # print (list_of_divs)
                for div in list_of_divs:
                        tag_h4 = div.find_all("h4")
                        # print (tag_h4)
                        for text in tag_h4:
                                # print (text)
                                if "Language:" in text:
                                        # print (text)
                                        tag_anchor = div.find_all("a")
                                        # print (tag_anchor)
                                        movie_language = [language.get_text() for language in tag_anchor]
                                        # print (movie_language)
                                elif "Country:" in text:
                                        # print (text)
                                        tag_anchor = div.find_all("a")
                                        # print (tag_anchor)
                                        movie_country = ([country.get_text() for country in tag_anchor])   # "".join
                                        # print (movie_country)
                movie_poster_list = soup.find("div", class_= "poster").a["href"]
                # print (movie_poster_list)
                movie_poster = "https://www.imdb.com" + movie_poster_list
                # print movie_poster
 
                movie_detail_div = {"name": "","director":"","bio":"","runtime":"","gener":"","language":"","country":"","poster_img_url":""}
                # print (movie_detail_div)
                movie_detail_div["name"] = movie_name
                movie_detail_div["director"] = movie_directors
                movie_detail_div["bio"] = movie_bio
                movie_detail_div["runtime"] = movie_runtime
                movie_detail_div["gener"] = movie_group
                movie_detail_div["language"] = movie_language
                movie_detail_div["country"] = movie_country
                movie_detail_div["poster_img_url"] = movie_poster
                with open(file_name , "w") as file:
                        file.write(json.dumps(movie_detail_div))
                return movie_detail_div
        
# url1 = scrept[0]["url"]
# movie_detail = scrap_movie_details(url1)
# pprint (movie_detail)

 
# task 5
def get_movie_list_details(movie_list):
        movie_list_details = []
        for i in movie_list:
                # print (movie_list)
                url = i["url"]
                # print (i)
                url_list = scrap_movie_details(url)
                # pprint (url_list)
                movie_list_details.append(url_list)
        return movie_list_details
get_movie_list = get_movie_list_details(scrept)
# pprint(get_movie_list)


# task 6
def analyse_movies_language(movie_detail_lang):
        movie_dict = {}
        for i in movie_detail_lang:
                # print (movie_detail_lang)
                if i not in movie_dict:
                        # print (movie_dict)
                        movie_dict[i] = 1
                        # print (movie_dict[i])
                else:
                        movie_dict[i] += 1
                        # print (movie_dict[i])
        return  movie_dict
movie_language_detail = []
for i in get_movie_list:
        # print(get_movie_list)
        lang = i["language"]
        # print(lang)
        movie_language_detail.extend(lang)
        # print (movie_language_detail)
        # print(lang)
language_count = analyse_movies_language(movie_language_detail) 
# pprint (language_count)


# task 7
def analyse_movies_directors(movie_detail_directors):
        movie_directors_detail = {}
        for i in movie_detail_directors:
                if i not in movie_directors_detail:
                        movie_directors_detail[i] = 1
                else:
                        movie_directors_detail[i] +=1
        return movie_directors_detail
movie_detail_of_directore = []
for i in get_movie_list:
        dire = i["director"]
        movie_detail_of_directore.extend(dire)
director_count = analyse_movies_directors(movie_detail_of_directore)
# pprint (director_count)


# task 10 
# from  Task5 import*
def analyse_language_and_directors(movie_list):
        director_dict = {}
        for movie in movie_list:
                # pprint (movie_list)
                # pprint (movie)
                for director in movie["director"]:
                        # print (director)
                        # print (movie["director"])
                        director_dict[director] = {}
                        # pprint (director_dict)
        for i in range(len(movie_list)):
                # print (i)
                # pprint (movie_list)
                for director in director_dict:
                        # print (director)
                        # pprint (director_dict)
                        if director in movie_list[i]["director"]:
                                # print (director)
                                # print (movie_list[i]["director"])
                                for language in movie_list[i]["language"]:
                                        # pprint (movie_list)
                                        # pprint (movie_list[i])
                                        # print (language)
                                        # print (movie_list[i]["language"])
                                        director_dict[director][language] = 0
                                        # print (director_dict[director][language])
        for i in range(len(movie_list)):
                # pprint (movie_list)
                # print (i)
                for director in director_dict:
                        # print (director)
                        # pprint (director_dict)
                        if director in movie_list[i]["director"]:
                                # print (director)
                                # print (movie_list[i]['director'])
                                # pprint (movie_list[i])
                                for language in movie_list[i]["language"]:
                                        # print (language)
                                        # print (movie_list[i]["language"])
                                        # pprint (movie_list[i])
                                        # pprint (movie_list)
                                        director_dict[director][language] = director_dict[director][language] + 1
                                        # pprint (director_dict)
                                        # print (director)
                                        # print (language)
                                        # print (director_dict[director][language])
        return director_dict
director_by_language = analyse_language_and_directors(get_movie_list)
# pprint (director_by_language)


# task 11

# from Task5 import* 
def analyse_movies_genre(movie_list):
        gener_dict = {}
        for movie in movie_list:
                # print (movie)
                # print (movie_list)
                for gener in movie['gener']:
                        # print (gener)
                        # print(movie['gener'])
                        if gener not in gener_dict:
                                # print(gener_dict)
                                gener_dict[gener] = 1
                                # print(gener_dict[gener])
                        else:
                                gener_dict[gener] += 1
                                # print(gener_dict[gener])
        return gener_dict
gener_analysis = (analyse_movies_genre(get_movie_list))
# pprint(gener_analysis)

# IMDB-caching