import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

URL = "https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"
def paytm_Pickles():
    sample = requests.get(URL)
    soup = BeautifulSoup(sample.text,"html.parser")
    # print(soup)
    tbody = soup.findAll("div", class_="_2i1r")
    # print(tbody)
    movie_list = []
    for i in tbody:
        new = {}
        pickles_link_poster = i.find("div", class_="_3nWP").img["src"]
        name = i.find("div",class_="_2apC").get_text()
        price = i.find("div",class_="_1kMS").get_text()
        link = i.find("a")
        pickles_link = "https://paytmmall.com/"+link["href"]
        new["pickles_link_poster"] = pickles_link_poster
        new["name"] = name
        new["price"] = price
        new["pickles_link"] = pickles_link
        movie_list.append(new)
        with open("pickles_caching.json","w") as fs:
            (json.dump(movie_list,fs,indent = 1))
    return movie_list
fun = paytm_Pickles()
pprint(fun)