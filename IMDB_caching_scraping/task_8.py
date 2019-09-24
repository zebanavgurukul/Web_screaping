from task_4 import scrap_movie_details
from task_4 import url1 as movie_url
from pprint import pprint
from pathlib import Path
import json

#task 8
def caching_movie_details(url): 
        Id = url.split("/")
        file_name_id = Id[5]
        file_name = "cahaing_8_" + file_name_id + ".json"
        # print (file_name)
        filepath = Path(file_name)
        if filepath.exists():
            print ("-=--=--=--=--=--=--=--=--=-- reading -=--=--=--=--=--=--=--=--")
            with open(file_name, "r") as file1:
                top_movie_read = file1.read()
                movies_lode = json.loads(top_movie_read)
                return movies_lode
        else:
            print ("-=--=--=--=--=--=--=--=--=--=-- writing -=--=--=--=--=--=--=--=--=")
            movie_data = scrap_movie_details(url)
            json_data = json.dumps(movie_data)
            with open(file_name,"w") as file:
                file.write(json_data)
            return movie_data
caching = caching_movie_details(movie_url)
# pprint(caching)