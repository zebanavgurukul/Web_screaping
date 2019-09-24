from task_4 import scrap_movie_details
from task_1 import scrept
from pprint import pprint
import random
import time

# task 5
def get_movie_list_details(movie_list):
        #task 9
        random_sleep = random.randint(1,3)
        #task 5
        movie_list_details = []
        for i in movie_list:
                url = i["url"]
                url_list = scrap_movie_details(url)
                movie_list_details.append(url_list)
                #task 9
                time.sleep(random_sleep)
                #task 5
        return (movie_list_details)
get_movie_list = get_movie_list_details(scrept[:250])
# pprint(get_movie_list)