import requests

class URLMaker():
    base_url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category, feature, **kwargs):
        url = f'{URLMaker.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'
        for key, val in kwargs.items():
            url += f'&{key}={val}'
        return url

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie_dict = res.json()

        if movie_dict.get('results'):
            return movie_dict.get('results')[0].get('id')
        else:
            return None


maker = URLMaker('7108d7a0290beb4c2d99634b041130ba')
# print(maker.get_url('movie', 'top_rated', region='KR'))
# print(maker.get_url('genre', 'movie/list', region='KR', language='ko'))
print(maker.movie_id('배트맨'))