import imp
import unittest

from .movie import *
from app.models import movie
Movie = movie.Movie


class MovieTest(unittest.TestCase):
    #tests the behaviour of the Movie class

    def setUp(self) -> None: #runs before every test
        
        self.new_movie = Movie(1234, 'Python is bae', 
            'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == '__main__':
    unittest.main()
