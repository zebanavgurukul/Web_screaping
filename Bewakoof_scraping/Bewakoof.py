from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
import requests
import json

url = "https://www.bewakoof.com/men-t-shirts"
def scraping_T_Shirts_For_Men(url_1):
    Id = url_1.split("/")
    file_name_id = Id[2]
    file_name = file_name_id + ".json"
    filepath = Path(file_name)
    if filepath.exists():
        print ("-=---=--=--=--=--=--=--=--=-- reading -=--=--=--=--=--=--=--=--")
        with open(file_name, "r") as file1:
            top_movie_read = file1.read()
            movies_lode = json.loads(top_movie_read)
        return movies_lode
    else:
        print ("-=--=--=--=--=--=--=--=--=--=-- writing -=--=--=--=--=--=--=--=--=")
        sample = requests.get(url_1)
        soup = BeautifulSoup(sample.text,"html.parser")
        categoryGridWrapper_clearfix = soup.find("div", class_= "categoryGridWrapper clearfix")
        productGrid = categoryGridWrapper_clearfix.find("div",class_="productGrid")
        new_list = []
        for i in productGrid:
            all_data = {}
            try:
                productCardImg_false = i.find("div", class_="productCardImg false")
                img = productCardImg_false.find("img")
            except AttributeError:
                continue
            try:
                poster = img["src"]
                # print(poster)
            except TypeError:
                continue
            title = i.find("img")
            name = title["title"]
            # print(name)
            price = i.find("div", class_ = "productPriceBox").b.get_text()
            # print(price)
            col_sm_4_col_xs_6 = i.a
            url = "https://www.bewakoof.com" + col_sm_4_col_xs_6["href"]
            # print(url)
            all_data["poster"] = poster
            all_data["name"] = name
            all_data["price"] = price
            all_data["url"] = url
            new_list.append(all_data)
        with open(file_name,"w") as fs:
            json_data = json.dumps(new_list)
            fs.write(json_data)
        return (new_list)
Bewakoof = scraping_T_Shirts_For_Men(url)
pprint(Bewakoof)