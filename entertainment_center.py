import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
                     


ef = media.Movie("EF",
                 "ef - a fairy tale of the two",
                 "https://upload.wikimedia.org/wikipedia/zh/4/4e/Ef_-_the_first_tale._cover.jpg",
                 "https://www.youtube.com/watch?v=tPmDKb836eo")

Wonder_woman = media.Movie("Wonder Woman",
                            "The origin of the wonder woman",
                            "https://upload.wikimedia.org/wikipedia/zh/b/b5/Wonder_Woman_2017_Poster.jpg",
                            "https://www.youtube.com/watch?v=5HUlW21v1fQ")

Dead_pool_2 = media.Movie("Dead Pool 2",
                           "The new story of Dead Pool",
                           "https://upload.wikimedia.org/wikipedia/zh/c/cf/Deadpool_2_poster.jpg",
                           "https://www.youtube.com/watch?v=Tpo9WYxLdLY")

movies = [avatar, ef, Wonder_woman, Dead_pool_2]
fresh_tomatoes.open_movies_page(movies)

