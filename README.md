kTorrent
=====
[![Build Status](https://travis-ci.org/codenirvana/kTorrent.svg)](https://travis-ci.org/codenirvana/kTorrent) [![PyPI version](https://badge.fury.io/py/ktorrent.svg)](https://badge.fury.io/py/ktorrent)

A Python module to fetch and parse data from Kickass Torrents.

Install
=====

### Using `pip`

```bash
$ pip install ktorrent
````

### Build from source

```bash
$ git clone git@github.com:codenirvana/ktorrent.git
$ cd ktorrent
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
search = torrent.search(search='linux', category='books', field='age', sorder='desc')

```

##### Function Parameters
- search = 'search query'
- category = 'torrent category'
- field = 'select field to sort results'
- sorder = 'sorting order'
- page = 'page number'

> All Parameters in String; No Order; Required: search

##### Valid Parameters Values
**category**
- all
- movies
- tv
- anime
- music
- books
- applications
- xxx

**field**
- size
- files
- age
- seed
- leech

**sorder**
- asc
- desc

Output
====

> JSON formatted search results, structure:

```json
{  
   "torrent":[  
      {  
         "name"     : "",
         "category" : "",
         "size"     : "",
         "files"    : "",
         "age"      : "",
         "seed"     : "",
         "leech"    : "",
         "link"     : ""
      }
    ]
}
```

Torrent Information Available
====
- name
- category
- size
- files
- age
- seed
- leech
- link

Todo
====
- [ ] Add number of pages
- [ ] Check if torrent varified or not
- [ ] Verify function parameters
- [ ] Download functionality


Licence
====
Open sourced under [MIT License](License.txt)
