#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Fab <Fab@pc24.home>
#
# Distributed under terms of the MIT license.

import fresh_tomatoes
import media

shutter = media.Movie("Shutter", "Thai scary movie","https://upload.wikimedia.org/wikipedia/en/4/45/Shutterposter.jpg","https://www.youtube.com/watch?v=XQ7rW3LXB5o")

dinner_de_cons = media.Movie("Le Dinner de Cons", "Dinner with someone stupid to enjoy time","https://upload.wikimedia.org/wikipedia/en/2/25/Le_d%C3%AEner_de_cons_(Poster).jpg","https://www.youtube.com/watch?v=u8FOJEzdYAs")

forrest_gump = media.Movie("Forrest Gump","Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.", "http://ia.media-imdb.com/images/M/MV5BMTI1Nzk1MzQwMV5BMl5BanBnXkFtZTYwODkxOTA5._V1_.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")

inception = media.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=RxabLA7UQ9k")

the_matrix = media.Movie("The Matrix", "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=gDadfh0ZdBM")

movies = [shutter, dinner_de_cons, the_matrix, inception, forrest_gump]
fresh_tomatoes.open_movies_page(movies)
