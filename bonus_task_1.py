from bs4 import BeautifulSoup
from pprint import pprint
import requests

URL = "https://www.imdb.com/title/tt0066763/"

def scrape_movie_details(url_movie):
    sample = requests.get(url_movie)
    soup = BeautifulSoup(sample.text,"html.parser")
    div = soup.find("div", class_="article", id = "titleRecs")
    recview = div.find("div", class_="rec_view")
    recpage = div.find("div", class_="rec_page")
    rec_item_rec_selected = div.findAll("div", class_= "rec_item")
    similar = []
    for i in rec_item_rec_selected:
        similar_movies = {}
        a = i.find("a")
        href = a.img["alt"]
        similar_movies["scrape_movies"] = href 
        similar.append(similar_movies)
    return(similar)
data_similar_movies = scrape_movie_details(URL)
pprint(data_similar_movies)