import webbrowser


class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        # initialinzg instance for opening the youtube video
        webbrowser.open(self.trailer_youtube_url)
