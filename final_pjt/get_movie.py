import requests

# 영화 id로 영화 제목 가져오기
def movie_title(movie_id):

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}'
    params = {
        'api_key' : 'c6d573e424ff520ecde3beacdc42ea62',
        'language' : 'ko',
    }
    res = requests.get(BASE_URL + path, params=params)
    data = res.json()
    return data['title']
    # return data
# print(movie_title(238))



# 영화 id로 영화 장르 가져오기
def movie_genres(movie_id):

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}'
    params = {
        'api_key' : 'c6d573e424ff520ecde3beacdc42ea62',
        'language' : 'en',
    }
    res = requests.get(BASE_URL + path, params=params)
    data = res.json()
    # return data['genres']
    return [item['name'] for item in data['genres']]

# top_rated 영화 60개(20개 * 3페이지)
def get_top():

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/top_rated'
    top_dict = {}
    for page in range(1, 7):
        params = {
            'api_key' : 'c6d573e424ff520ecde3beacdc42ea62',
            'language' : 'ko',
            'page' : page,
        }
        res = requests.get(BASE_URL + path, params=params)
        data = res.json()
        result = data['results']
        
        for r in result:
            top_dict[r['id']] = r['title']
    return top_dict
    
# print(get_top())


#  popular 영화 60개(20개 * 3페이지)
def get_pop():

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    pop_dict = {}
    for page in range(1, 6):
        params = {
            'api_key' : 'c6d573e424ff520ecde3beacdc42ea62',
            'language' : 'ko',
            'page' : page,
        }
        res = requests.get(BASE_URL + path, params=params)
        data = res.json()
        result = data['results']
        
        for r in result:
            pop_dict[r['id']] = r['title']
    return pop_dict
    
# print(get_pop())


# 영화 id호 해당 영화 키워드 불러오기 (키워드가 10개 이상인 영화만)
def get_keywords(movie_id):

    BASE_URL = f"https://api.themoviedb.org/3/movie/{movie_id}/keywords"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNmQ1NzNlNDI0ZmY1MjBlY2RlM2JlYWNkYzQyZWE2MiIsInN1YiI6IjY0NWRhMDQwODhiMTQ4MDExOWQ3NzIwMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.m6gDYat0dQCQO2irJz1OpNBq-u4pWi6-fvJVyphHSEw"
    }

    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    return data["keywords"]

for key in get_top().keys():
    if len(get_keywords(key)) >= 10:
        keywords =  [i for i in movie_genres(key)]+[item['name'] for item in get_keywords(key)]
        movie_words_top = {movie_title(key): keywords}
        print(movie_words_top)

for key in get_pop().keys():
    if len(get_keywords(key)) >= 10:
        keywords = {movie_title(key): [i for i in movie_genres(key)]+[item['name'] for item in get_keywords(key)]}
        movie_words_pop = {movie_title(key): keywords}
        print(movie_words_pop)


