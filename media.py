import webbrowser

class Movie(object):
	"""docstring for Movie"""
	def __init__(self, title, story, poster, trailer):
		self.title = title
		self.story = story
		self.poster = poster
		self.trailer = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_url)
