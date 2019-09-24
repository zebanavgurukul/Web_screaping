from task_5_9 import get_movie_list
from pprint import pprint

#task 11
def analyse_movies_directors(movie_detail_directors):
        movie_directors_detail = {}
        for i in movie_detail_directors:
                if i not in movie_directors_detail:
                        movie_directors_detail[i] = 1
                else:
                        movie_directors_detail[i] = movie_directors_detail[i] + 1
        return movie_directors_detail
movie_detail_of_directore = []
for i in get_movie_list:
        dire = i["Drama"]
        movie_detail_of_directore.extend(dire)
Drama_count = analyse_movies_directors(movie_detail_of_directore)
# pprint (Drama_count)