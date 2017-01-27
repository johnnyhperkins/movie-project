import webbrowser

## Create the Movie class
class Movie():
    """ This class creates instances of movies """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, description):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.description = description

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
