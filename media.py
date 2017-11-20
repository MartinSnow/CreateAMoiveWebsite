class Movie():

    '''This is a class called Movie, it contains movie's name, summary information, poster picture and trailer.'''
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''This function will create an instance of the Movie class.
           The instance contains the movie's name, summary information, posterpicture and trailer.'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
