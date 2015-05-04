import webbrowser

class Movie():
	"""Receptacle for movie information."""
	def __init__(self, -Title, Story, Poster, Trailer, Year, Actors, Genre, imdbRating, Runtime, Rated):
		self.title = Title
		self.story = Story
		self.poster = Poster
		self.trailer_url = Trailer
		self.year = Year
		self.actors = Actors
		self.genre = Genre
		self.rated = Rated
		self.imdbRating = imdbRating
		self.runTime = Runtime

	def show_trailer(self):
		"""Open movie trailer in browser window."""
		webbrowser.open(self.trailer_url)
