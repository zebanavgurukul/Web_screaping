from task_13 import details_Cast
from pprint import pprint


def analyse_co_actors(movies_list):
    dict_cast = {}
    for index in movies_list:
        cast_data = index["cast"]
        name = cast_data[0]["Name"]
        imdb_id = cast_data[0]["imdb_id"]
        for movie in movies_list:
            castList = movie["cast"]
            if imdb_id == castList[0]["imdb_id"]:
                if imdb_id not in dict_cast:
                    dict_cast[imdb_id] = {}
                    dict_cast[imdb_id]["Name"] = name
                    dict_cast[imdb_id]["frequent_co_actors"] = []
                    co_Director = {}
                    co_Director["num_movie"] = 1
                    co_Director["imdb_id"] = castList[1]["imdb_id"]
                    co_Director["Name"] = castList[1]["Name"]
                    dict_cast[imdb_id]["frequent_co_actors"].append(co_Director)
                else:
                    num = 1
                    for frequent_co_actor in dict_cast[imdb_id]["frequent_co_actors"]:
                        if frequent_co_actor["imdb_id"] == castList[1]["imdb_id"]:
                            frequent_co_actor["num_movie"] castList= frequent_co_actor["num_movie"] + 1
                            break
                        num = num + 1
                    if num == len(dict_cast[imdb_id]["frequent_co_actors"]):
                        co_Director = {}
                        co_Director["imdb_id"] = castList[1]["imdb_id"]
                        co_Director["Name"] = castList[1]["Name"]
                        co_Director["num_movie"] = 1
                        dict_cast[imdb_id]["frequent_co_actors"].append(co_Director)  
    return(dict_cast)
actors_actresses = analyse_co_actors(details_Cast)  
pprint(actors_actresses)