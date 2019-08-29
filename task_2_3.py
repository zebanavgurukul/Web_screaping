from task_1 import scrept
from pprint import pprint

# task 2
def group_by_year(movies):
        movie_dict = {}
        years = []
        for i in movies:
                year = i["year"]
                if year not in years:
                        years.append(year)
        for i in years:
            movie_dict[i] = {}
        for i in movies:
                year = i["year"]
                for x in movie_dict:
                        if str(x) == str(year):
                                movie_dict[x].append(i)
        return movie_dict
dec_arg = group_by_year(scrept)
# pprint (dec_arg)


# task 3
def group_by_decade(movies):
        moviedec = {}
        list1 = []
        for index in movies:
                mod = index % 10
                decade = index - mod
                if decade not in list1:
                        list1.append(decade)
        list1.sort()
        for i in list1:
                moviedec[i] = []
        for i in moviedec:
                dec10 = i + 9
                for x in movies:
                        if x <= dec10 and x >= i:
                                for v in movies[x]:
                                        moviedec[i].append(v)
        return (moviedec)
movie_group = group_by_decade(dec_arg)
# pprint (movie_group)