from task_13 import details_Cast
from pprint import pprint

def analyse_actors(movies_list):
    dict_cast = {}
    for index in movies_list:
        cast_data = index['cast']
        for actor in cast_data:
            name = actor["Name"]
            imdb_id = actor["imdb_id"]
            for movie in movies_list:
                castList = movie["cast"]
                for cast_name in castList:
                    if imdb_id == cast_name["imdb_id"]:
                        if imdb_id not in dict_cast:
                            dict_cast[imdb_id] = {}
                            dict_cast[imdb_id]["Name"] = name
                            dict_cast[imdb_id]["num_movie"] = 1
                        else:
                            dict_cast[imdb_id]["num_movie"] = dict_cast[imdb_id]["num_movie"] + 1
    return (dict_cast)
All_cast = analyse_actors(details_Cast)
# pprint(All_cast)
