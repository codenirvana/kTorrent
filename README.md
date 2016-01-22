kTorrent
=====
[![version](https://img.shields.io/pypi/status/ktorrent.svg)](https://pypi.python.org/pypi/ktorrent/)
[![version](https://img.shields.io/pypi/v/ktorrent.svg)](https://pypi.python.org/pypi/ktorrent/)
[![supported](https://img.shields.io/pypi/pyversions/ktorrent.svg)](https://pypi.python.org/pypi/ktorrent/)
[![Build Status](https://travis-ci.org/codenirvana/kTorrent.svg)](https://travis-ci.org/codenirvana/kTorrent)

A Python module to fetch and parse data from Kickass Torrents.

Install
=====

### Using `pip`

```bash
$ pip install ktorrent
````

### Build from source

```bash
$ git clone https://github.com/codenirvana/kTorrent.git
$ cd kTorrent
$ python setup.py install
```

Usage
====

### Search

```python
import ktorrent

# Basic Search
search = ktorrent.search(search='Linux')

# Complex Search
search = ktorrent.search(search='Linux Shell script', strict=1, category='books', field='age', sorder='desc', page=2)
```

##### Function Parameters
- **search**    = 'search query'
- **strict**    = 'search strictness' **[int]**
- **safe**      = 'family safety filter' **[int]**
- **verified**  = 'only verified torrents' **[int]**
- **subtract**  = 'Subtract specified word(s)'
- **user**      = 'Uploads by certain user'
- **category**  = 'torrent category'
- **field**     = 'select field to sort results'
- **sorder**    = 'sorting order'
- **page**      = 'page number' **[int]**

> Required: search

##### Valid Parameters Values

* Search Result Ordering

   category     | field | sorder
   ------------ | ----- | ------
   all          | size  |  asc
   movies       | files |  desc
   tv           | age   |
   anime        | seed  |
   music        | leech |
   books        |
   applications |
   games        |
   other        |
   xxx          |

* Search Filters

   *value* | strict | safe | verified
   ------- | ------ | ---- | --------
      -1   | fuzzy  |   -  |    -
      0    | normal |   -  |    -
      1    | strict | yes  |   yes

* **subtract** : Space separated, *... subtract='book reference'...*

* **user** : Single user/uploader name


### Top

```python
import ktorrent

# Top books
top_books = ktorrent.top(category='books')

# Top movies
top_movies = ktorrent.top(category='movies', page=2)
```

##### Function Parameters
- **category**  = 'torrent category'
- **page**      = 'page number' **[int]**

> Required: category

##### Valid Parameters Values

* Categories available

   movies, tv, anime, music, books, applications, games, other, xxx


Output
====

> JSON formatted search results, structure:

```json
{  
   "status" : 200,
   "meta":{  
      "pageCurrent" : 1,
      "pageResult"  : 25,
      "pageTotal"   : 10
   },
   "torrent":[  
      {  
         "age"      : "",
         "category" : "",
         "files"    : "",
         "leech"    : "",
         "link"     : "",
         "magnet"   : "",
         "name"     : "",
         "seed"     : "",
         "size"     : "",
         "verified" : ""
      }
    ]
}
```

ToDo
====
- [ ] multiple tests for verification

Licence
====
Open sourced under [MIT License](LICENSE)
