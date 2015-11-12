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
search = ktorrent.search(search='linux', category='books', field='age', sorder='desc')
```

##### Function Parameters
- **search** = 'search query'
- **category** = 'torrent category'
- **field** = 'select field to sort results'
- **sorder** = 'sorting order'
- **page** = 'page number'

> All Parameters in String; No Order; Required: search

##### Valid Parameters Values
category     | field | sorder
------------ | ----- | ------
all          | size  |  asc
movies       | files |  desc
tv           | age   |
anime        | seed  |
music        | leech |
books        |
applications |
xxx          |

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

Todo
====
- [ ] Document Code
- [ ] Add number of pages
- [ ] Check if torrent verified or not
- [ ] Verify function parameters
- [ ] Download functionality


Licence
====
Open sourced under [MIT License](LICENSE)
