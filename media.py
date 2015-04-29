import webbrowser

class Movie():
	"""Receptacle for movie information."""
	def __init__(self, title, story, poster, trailer, year, actors, genre, imdbRating, runTime, rating):
		self.title = title
		self.story = story
		self.poster = poster
		self.trailer_url = trailer
		self.year = year
		self.actors = actors
		self.genre = genre
		self.rating = rating
		self.imdbRating = imdbRating
		self.runTime = runTime

	def show_trailer(self):
		webbrowser.open(self.trailer_url)
