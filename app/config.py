from distutils.debug import DEBUG


from instance.config import MOVIE_API_KEY


class Config: #parent class
    
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=e9fbc82fc923aae1ebc65d83e13b2d52'


class ProdConfig: #child to  Config

    pass

class DevConfig: #child to Config

    DEBUG = True



