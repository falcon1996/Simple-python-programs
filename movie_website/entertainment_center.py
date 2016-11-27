import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Story of a boy and his toys that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")                  # movie is name of file and Movie is class in that file


avatar = media.Movie("Avatar","A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


gravity = media.Movie("Gravity", "seemingly routine spacewalk, disaster strikes.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                             "https://www.youtube.com/watch?v=OiTiKOy59o4")

interstellar = media.Movie("Interstellar", "crew of astronauts travel through a wormhole in search of a new home for humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg","https://www.youtube.com/watch?v=3WzHXI5HizQ")

martian = media.Movie("The martian","Survival of an astronaut left alone in mars",
                     "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                     "https://www.youtube.com/watch?v=ej3ioOneTy8")


inception = media.Movie("Inception", "One last job could give him his life back but only if he can accomplish the impossible - inception.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

movies = [toy_story, avatar, gravity, interstellar, martian, inception]
fresh_tomatoes.open_movies_page(movies)
