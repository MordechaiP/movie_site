import webbrowser

class Movie():
	"""docstring for Movie"""
	def __init__(self, title, story, poster, trailer):
		self.title = title
		self.story = story
		self.poster = poster
		self.trailer_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_url)
