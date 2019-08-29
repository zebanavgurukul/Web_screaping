from bs4 import BeautifulSoup
from task_1 import scrept
from pprint import pprint
import requests

# task 4
def scrap_movie_details(movie_url):
        page = requests.get(movie_url)
        soup = BeautifulSoup(page.text,"html.parser") 
        title_div = soup.find("div", class_ = "title_bar_wrapper").h1.get_text().split('(')
        movie_name = title_div[0]
        # print (movie_name)
        
        sub_div = soup.find("div", class_ = "subtext")
        runtime = sub_div.find("time").get_text().strip()
        runtime_hours = int(runtime[0])*60
        #     print (runtime_hours)
        gener = sub_div.find_all("a")
        gener.pop()
        group = []
        for i in gener:
                movie_group = i.get_text()
                group.append(movie_group)
        #     print(group)
        sumary = soup.find("div", class_= "plot_summary")
        movie_bio = sumary.find("div", class_= "summary_text").get_text().strip()
        # print (movie_bio)
        director = sumary.find("div", class_= "credit_summary_item")
        director_list = director.find_all("a")
        director = []
        for i in director_list:
                movie_directors = i.get_text().strip()
                director.append(movie_directors)
        #     print (director)
        extra_details = soup.find("div", attrs = {"class":"article","id":"titleDetails"})
        list_of_divs = extra_details.find_all("div")
        language_data = []
        country_data = []
        for div in list_of_divs:
                tag_h4 = div.find_all("h4")
                for text in tag_h4:
                        if "Language:" in text:
                                tag_anchor = div.find_all("a")
                                for language in tag_anchor:
                                        movie_language = language.get_text()
                                        language_data.append(movie_language)
                                #     print(language_data)
                        elif "Country:" in text:
                                tag_anchor = div.find_all("a")
                                for country in tag_anchor:
                                        movie_country = country.get_text()
                                        country_data.append(movie_country)
                                #     print(country_data)
        movie_poster_list = soup.find("div", class_= "poster").a["href"]
        movie_poster = "https://www.imdb.com" + movie_poster_list
        # print (movie_poster)

        movie_detail_div = {"name": "","director":"","bio":"","runtime":"","gener":"","language":"","country":"","poster_img_url":""}
        
        movie_detail_div["name"] = movie_name
        movie_detail_div["director"] = director
        movie_detail_div["bio"] = movie_bio
        movie_detail_div["runtime"] = runtime_hours
        movie_detail_div["gener"] = group
        movie_detail_div["language"] = language_data
        movie_detail_div["country"] = country_data
        movie_detail_div["poster_img_url"] = movie_poster
        return movie_detail_div
        
url1 = scrept[1]["url"]
movie_detail = scrap_movie_details(url1)
# pprint (movie_detail)