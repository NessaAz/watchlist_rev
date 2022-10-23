from turtle import title
from app import app
import urllib.request, json
from .models import movie


Movie = movie.Movie

api_key = app.config['MOVIE_API_KEY']
base_url = app.config["MOVIE_API_BASE_URL"] #movie base url


def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def process_results(movie_list):
    #processes movie results and transforms them to a list of Obj
    movie_results = []

    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results


def get_movies(cateegory):
    #function that gets the json response to our url req
    get_movies_url = base_url.format(cateegory, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response ['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

