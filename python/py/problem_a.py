import requests
from tmdb import URLMaker
from pprint import pprint

def top_rated_movie():
    maker = URLMaker('7108d7a0290beb4c2d99634b041130ba')
    url = maker.get_url('movie', 'top_rated')
    res = requests.get(url)
    movie_dict = res.json()
    mobie_list = movie_dict.get('results')

    result = []
    for movie in mobie_list:
        result.append(movie['title'])
    
    return result

pprint(top_rated_movie())
    