from task_4 import scrap_movie_details
from task_1 import scrept
from task_12 import caching_movie_details
from pprint import pprint


def movie_details_Cast(url2):
    movie_list_cast = []
    for i in url2:
        url = i["url"]
        movie_Details = scrap_movie_details(url)
        cast = caching_movie_details(url)
        movie_Details["cast"] = cast
        movie_list_cast.append(movie_Details)
    return movie_list_cast
details_Cast = movie_details_Cast(scrept[:250])
# pprint (details_Cast)