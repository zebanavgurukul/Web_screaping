from bs4 import BeautifulSoup
from pprint import pprint
import requests

URL = "https://www.imdb.com/india/top-rated-indian-movies/" 
def scrap_to_tist():
        sample = requests.get(URL)
        soup = BeautifulSoup(sample.text,"html.parser") 
        tbody = soup.find("tbody",class_ = "lister-list")
        trs = tbody.findAll('tr')
        movie_list = []
        j = 0
        for i in trs:
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
        return movie_list
scrept = scrap_to_tist()
# pprint (scrept) 