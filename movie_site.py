import webbrowser
import os
import re

import media

from pymongo import MongoClient

# Styles and scripting for the page
main_page_head = '''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Favorite Movies</title>

    <link rel="stylesheet" href="movie_site.css">

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="movie_site.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>

	<!-- Main Page Content -->
	<header id="logo">
	  <h1>Favorite Movie Trailers</h1>
	</header>
	<section id="main">
		<article>
			<ul class="movie">
				{movie_tiles}
			</ul>
		</article>
	</section>

	<!-- Trailer Video Modal -->
	<section id="modal">
		<div id="modal-inner">
			<header>
				<button id="modal-close"></button>
			</header>
			<div id="video-container"></div>
		</div>
	</section>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<li data-trailer-youtube-id="{trailer}">
    <img class="poster" src="{poster}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div class="more_info closed">
    	<button class="more_btn">More Info</button>
		<button class="less_btn">Less Info</button>
		<dl>
			<dt>Year:</dt>
			<dd>{year}</dd>
			<dt>Genre:</dt>
			<dd>{genre}</dd>
			<dt>Rating:</dt>
			<dd>{rating}</dd>
			<dt>Story:</dt>
			<dd>{story}</dd>
			<dt>Run Time:</dt>
			<dd>{runTime}</dd>
			<dt>Actors:</dt>
			<dd>{actors}</dd>
			<dt>IMDB Rating:</dt>
			<dd>{imdbRating}</dd>
		</dl>
    </div>
</li>
'''

# Load movies from database and use relevant field to initiate Movie instances. The collection of movies are stored in a list.
client = MongoClient('mongodb://localhost:27017/')
db = client["movie_site"]
movies = []
for m in db.movies.find():
	movies.append(media.Movie(title=m['Title'], story=m['Plot'], poster=m['Poster'], trailer=m['Trailer'],year=m['Year'],
		actors=m['Actors'], genre=m['Genre'], imdbRating=m['imdbRating'], runTime=m['Runtime'], rating=m['Rated']))



#
# Following two functions were taken from fresh_tomates.py with only minor changes
#

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster = movie.poster,
            trailer = trailer_youtube_id,
            year = movie.year,
            story = movie.story,
			actors = movie.actors,
			genre = movie.genre,
			rating = movie.rating,
			imdbRating = movie.imdbRating,
			runTime = movie.runTime
        )
    return content

def open_movies_page(movies):
	# Create or overwrite the output file
	output_file = open('movie_site.html', 'w')

	# Replace the placeholder for the movie tiles with the actual dynamically generated content
	rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

	# Output the file
	output_file.write(main_page_head + rendered_content)
	output_file.close()

	# open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2) # open in a new tab, if possible



open_movies_page(movies)