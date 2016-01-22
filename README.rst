========
kTorrent
========

A Python module to fetch and parse data from Kickass Torrents.

Install
-------

    ``pip install ktorrent``

Usage
-----
# Import Library
 >>> import ktorrent

# Basic Search
 >>> search = ktorrent.search(search='Linux')

# Complex Search
 >>> search = ktorrent.search(search='Linux Shell script', strict=1, category='books', field='age', sorder='desc', page=2)

# Top movies
 >>> top_movies = ktorrent.top(category='movies', page=2)

Know More
=========

kTorrent Docs: https://github.com/codenirvana/kTorrent#readme
