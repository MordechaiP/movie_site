import fresh_tomatoes
import media

so2001 = media.Movie("2001: A Space Odyssey",
			   "Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
			   "https://image.tmdb.org/t/p/w396/rT9w3tzk25jA8vl7KyvzUP5gHJV.jpg",
			   "https://youtu.be/XHjIqQBsPjk")

jedi = media.Movie("Return of the Jedi",
			 "After rescuing Han Solo from the palace of Jabba the Hutt, the rebels attempt to destroy the second Death Star, while Luke struggles to make Vader return from the dark side of the Force.",
			 "http://img1.wikia.nocookie.net/__cb20050925102019/starwars/images/4/44/Return_of_the_jedi_old.jpg",
			 "https://youtu.be/5UfA_aKBGMc")
forbidden_planet = media.Movie("Forbidden Planet",
				"A starship crew goes to investigate the silence of a planet's colony only to find two survivors and a deadly secret that one of them has.",
				"http://ayay.co.uk/movies/poster/sci_fi/forbidden-planet-3.jpg",
				"https://youtu.be/8y4crGU7dkg")
wrath_of_khan = media.Movie("Star Trek II: The Wrath of Khan",
				"With the assistance of the Enterprise crew, Admiral Kirk must stop an old nemesis, Khan Noonien Singh, from using his son's life-generating device, the Genesis Device, as the ultimate weapon.",
				"http://photos.imageevent.com/afap/wallpapers/movies/startrek/Star-Trek-The-Wrath-Of-Khan_2.jpg",
				"https://youtu.be/UJTi7KJPx_E")
giant_shadow = media.Movie("Cast a Giant Shadow",
				"An American Army officer is recruited by the yet to exist Israel to help them form an army. He is disturbed by this sudden appeal to his jewish roots. Each of Israel's Arab neighbors has vowed to invade the poorly prepared country as soon as partition is granted. He is made commander of the Israeli forces just before the war begins. ",
				"http://upload.wikimedia.org/wikipedia/en/9/9e/Cast_original.jpg",
				"https://youtu.be/5AhsTY5_1hE")
citizen_kane = media.Movie("Citizen Kane",
				"Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance.",
				"http://upload.wikimedia.org/wikipedia/en/c/ce/Citizenkane.jpg",
				"https://youtu.be/zyv19bg0scg")

movies = [so2001, jedi, forbidden_planet, wrath_of_khan, giant_shadow, citizen_kane]
#so2001.show_trailer()
fresh_tomatoes.open_movies_page(movies)
