from bs4 import BeautifulSoup
from task_1 import scrept
from pprint import pprint
import requests


def scrape_movie_details(url_movie):
    similar = []
    # similar_movies = {}
    for i in url_movie:
        similar_movies = {}
        url = i["url"]
        sample = requests.get(url)
        soup = BeautifulSoup(sample.text,"html.parser")
        div = soup.find("div", class_="article", id = "titleRecs")
        recview = div.find("div", class_="rec_view")
        recpage = div.find("div", class_="rec_page")
        rec_item_rec_selected = div.findAll("div", class_= "rec_item")
        try:
            for i in rec_item_rec_selected:
                a = i.find("a")
                href = a.img["alt"]
                # pprint(href)
        except TypeError:
                continue
        similar_movies["scrape_movies"] = href 
        similar.append(similar_movies)
    return (similar)
all_data = scrape_movie_details(scrept)
pprint(all_data)