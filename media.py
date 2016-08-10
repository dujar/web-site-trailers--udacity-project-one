#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Fab <Fab@pc24.home>
#
# Distributed under terms of the MIT license.

class Movie():
    def __init__(self, movie_title,movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyiline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
