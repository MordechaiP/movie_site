import webbrowser

class Movie():
	"""Receptacle for movie information."""
	def __init__(self, args):
		self.title = args["Title"]
		self.story = args["Plot"]
		self.poster = args["Poster"]
		self.trailer_url = args["Trailer"]
		self.year = args["Year"]
		self.actors =args["Actors"]
		self.genre = args["Genre"]
		self.rating = args["Rated"]
		self.imdbRating = args["imdbRating"]
		self.runTime = args["Runtime"]

	def show_trailer(self):
		"""Open movie trailer in browser window."""
		webbrowser.open(self.trailer_url)
