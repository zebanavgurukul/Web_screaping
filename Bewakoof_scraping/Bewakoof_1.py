from bs4 import BeautifulSoup
from pprint import pprint
import requests

url = "https://www.bewakoof.com/men-t-shirts"

def scraping_T_Shirts_For_Men(url_1):
    sample = requests.get(url_1)
    soup = BeautifulSoup(sample.text,"html.parser")
    categoryGridWrapper_clearfix = soup.find("div", class_= "categoryGridWrapper clearfix")
    productGrid = categoryGridWrapper_clearfix.find("div", class_="productGrid")
    # new_list = []
    for index in productGrid:
        # all_data = {}
        try:
            productCardImg_false = index.find("div", class_="productCardImg false")
            img = productCardImg_false.find("img")
            pprint(img)
        except AttributeError:
            continue
    #     try:
    #         poster = img["src"]
    #         # pprint(poster)
    #     except TypeError:
    #         continue
    #     title = index.find("img")
    #     name = title["title"]
    #     # print(name)
    #     price = index.find("div", class_ = "productPriceBox").b.get_text()
    #     # print(price)
    #     col_sm_4_col_xs_6 = index.a
    #     url = "https://www.bewakoof.com" + col_sm_4_col_xs_6["href"]
    #     # print(url)
    #     all_data["poster"] = poster
    #     all_data["name"] = name
    #     all_data["price"] = price
    #     all_data["url"] = url
    #     new_list.append(all_data)
    # return(new_list)
scraping_T_Shirts_For_Men(url)
# pprint(Bewakoof)