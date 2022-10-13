from email import message
from flask import render_template


from app import app
from .request import *

@app.route('/')
def index():

    title = 'welcome to the best site views'

    popular_movies = get_movies('popular')
    print(popular_movies)

    return render_template('index.html',
        title = title,
        popular = popular_movies,
    )


@app.route('/movie/<int:movie_id>/')
def movie(movie_id):


    return render_template('movie.html',
        id = movie_id
    )