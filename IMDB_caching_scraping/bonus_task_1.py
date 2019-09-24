from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
import requests
import json

URL = "https://www.imdb.com/title/tt0066763/"
def scrape_movie_details(url_movie):
    Id = url_movie.split("/")
    file_name_id = Id[5]
    file_name = "cahaing_bonus_" + file_name_id + ".json"
    filepath = Path(file_name)
    if filepath.exists():
        print ("-=---=--=--=--=--=--=--=--=-- reading -=--=--=--=--=--=--=--=--")
        with open(file_name, "r") as file1:
            top_movie_read = file1.read()
            movies_lode = json.loads(top_movie_read)
        return movies_lode
    else:
        print ("-=--=--=--=--=--=--=--=--=--=-- writing -=--=--=--=--=--=--=--=--=")
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
        with open(file_name,"w") as fs:
            json_data = json.dumps(similar)
            fs.write(json_data)
        return (similar)
data_similar_movies = scrape_movie_details(URL)
pprint(data_similar_movies)