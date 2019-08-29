from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
import requests
import json

#task 12 
movie_url = "https://www.imdb.com//title/tt0066763/"
def caching_movie_details(url): 
        Id = url.split("/")
        file_name_id = Id[5]
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
                page = requests.get(url)
                soup = BeautifulSoup(page.text,"html.parser")
                div_data = soup.find("div", class_="article", id = "titleCast")
                table_data = div_data.find("table", class_="cast_list")
                tr_data_odd = table_data.findAll("tr", class_="odd")        
                tr_data_even = table_data.findAll("tr", class_="even")
                list_name_id = []
                for odd in tr_data_odd:
                        dict_odd_Id = {}
                        td_data = odd.findAll('td')
                        Link = td_data[1].a['href']
                        split = Link.split('/')
                        cast_id = split[2]
                        name_data = td_data[1].a.get_text()
                        name = name_data.strip()
                        dict_odd_Id["imdb_id"] = cast_id
                        dict_odd_Id['Name'] = name
                        list_name_id.append(dict_odd_Id)
                for odd in tr_data_even:
                        dict_even_Id = {}
                        td_data = odd.findAll('td')
                        Link = td_data[1].a['href']
                        split = Link.split('/')
                        cast_id = split[2]
                        name_data = td_data[1].a.get_text()
                        name = name_data.strip()
                        dict_even_Id["imdb_id"] = cast_id
                        dict_even_Id['Name'] = name
                        list_name_id.append(dict_even_Id)
                with open(file_name,"w") as fs:
                        json_data = json.dumps(list_name_id)
                        fs.write(json_data)
                return (list_name_id)
list_name_id_all = caching_movie_details(movie_url)
# pprint(list_name_id_all)
