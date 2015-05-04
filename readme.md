# movie_site

movie_site.py

Loads a list of movies, with various details (see below), from movies.json to populate Movie instances (see media.py, below), creates movie_site.html, and opens it browser window. The site shows a collection of movie posters, which when clicked, launches a Youtube tailer. Also provided are additional details which can be viewed by clicking on the "More Info" button.

To generate a new version of movie_site.html, place in movies.json one json object per movie. See below for required fields.


movie_site.css
movie_site.js

Helper files for movie_site.html


movies.json

A file containing one json object for each desired movie. Object can optionally be seperated be white space.

media.py

Provides a Movie class for store various details about a movie. Required fields are: Title, Story, Poster, Trailer, Year, Actors, Genre, imdbRating, Runtime, and Rated.

Also provided is show_trailer() method which opens the accocated trailer in a browser.