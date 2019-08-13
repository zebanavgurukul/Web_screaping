import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

link = "https://www.ndtv.com/latest/page-1"
def india_news(data):
    request_1 = requests.get(data)
    soup_1 = BeautifulSoup(request_1.text,"html.parser")
    All_data = soup_1.find("div",class_="ins_left_rhs")
    ul = All_data.find('ul')
    li_data = ul.findAll("li")
    new_list = []
    for i in li_data: 
        all_data = {}
        try:   
            h4_data = i.find("div",class_="nstory_header")
            link_data = h4_data.find("a")
            link = link_data["href"]
            # print(link)
        except AttributeError:
            continue
        try:
            request = requests.get(link)
            soup = BeautifulSoup(request.text,"html.parser")
            div_data = soup.find("div",class_="ins_lftcont640 clr",id ="newsDescriptionContainer").div.get_text()
            Updated = soup.find("div",class_="ins_dateline").get_text()
            data = Updated.split("|")
            news_Updated = (data[2])
            # print(news_Updated)
        except AttributeError:
            continue
        try:
            news_bio = soup.find("div",class_="ins_storybody",id="ins_storybody").p.get_text()
            # print(news_bio)
            divdata = soup.find("div",class_="ins_dateline")
            a_data = divdata("a")
            url_index = a_data[1]
            Edited_by = url_index.find("span").span.get_text()
            # print(Edited_by)
        except AttributeError:
            continue
        all_data["link"] = link
        all_data["news_Updated"] = news_Updated
        all_data["news_bio"] = news_bio
        all_data["Edited_by"] = Edited_by
        new_list.append(all_data)
        with open("india_news_caching.json","w") as fs:
            (json.dump(new_list,fs,indent = 1))
    return (new_list)
more_data = india_news(link)
pprint(more_data)



