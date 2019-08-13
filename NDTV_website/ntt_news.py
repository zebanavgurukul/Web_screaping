import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

link = "https://www.ndtv.com/india?pfrom=home-mainnavgation"
def india_news(url):
    new_list = []
    request = requests.get(url)
    soup = BeautifulSoup(request.text,"html.parser")
    All_data = soup.find("div",class_="ins_left_rhs")
    ul = All_data.find('ul')
    li_data = ul.findAll("li")
    for i in li_data: 
        all_data = {}
        try:   
                h4_data = i.find("div",class_="nstory_header")
                link_data = h4_data.find("a")
                link = link_data["href"]
                # print(link)
        except AttributeError:
                continue
        request_1 = requests.get(link)
        soup_1 = BeautifulSoup(request_1.text,"html.parser")
        h1_data = soup_1.find("div",class_="ins_wid990").h1.get_text()
        # print(h1_data)
        Updated = soup_1.find("div",class_="ins_dateline").get_text()
        data = Updated.split("|")
        news_edited = (data[1])
        # print(news_edited)
        news_Updated = (data[2])
        # print(news_Updated)
        try:
                news_bio = soup_1.find("div",class_="ins_storybody").get_text()
                # print(news_bio)
        except AttributeError:
                continue
        all_data["link"] = link
        all_data["h1_data"] = h1_data
        all_data["news_edited"] = news_edited
        all_data["news_Updated"] = news_Updated
        all_data["news_bio"] = news_bio
        new_list.append(all_data)
        with open("india_news.json","w") as fs:
            (json.dump(new_list,fs,indent = 1))
    return(new_list)
man_data = india_news(link)
pprint(man_data)