import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

URL = "https://www.giveindia.org/certified-indian-ngos"
def give_function():
    ng_all = [] 
    
    request = requests.get(URL)
    soup = BeautifulSoup(request.text,"html.parser")
    table_data = soup.find("table",class_="jsx-697282504 certified-ngo-table")
    tr_data = table_data.findAll("tr",class_="jsx-697282504")
    # print(tr_data)
    for i in tr_data:
        new = {}
        name = i.find('div', class_='col')
        if name is not None:
            ngo_name = name.get_text()
            # print(ngo_name)

        try:
            td_list = i.find_all('td')[1]
        except IndexError:
            continue
        work = ''.join(td_list.contents)
        # print(work)

        try:
            state_data = i.find_all('td')[2]
        except IndexError:
            continue
        state = ''.join(state_data.contents)
        # print(state)
        new["ngo_name"] = ngo_name
        new["work"] = work
        new["state"] = state
        ng_all.append(new)
        with open("ngo_caching.json","w") as fs:
            (json.dump(ng_all,fs,indent = 1))
    return (ng_all)
ng_data = give_function()
pprint(ng_data)