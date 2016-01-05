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
search = ktorrent.search(search='Linux Shell script', strict='1', category='books', field='age', sorder='desc', page='2')
```

##### Function Parameters
- **search** = 'search query'
- **strict** = 'search strictness'
- **category** = 'torrent category'
- **field** = 'select field to sort results'
- **sorder** = 'sorting order'
- **page** = 'page number'

> All Parameters in String; No Order; Required: search

##### Valid Parameters Values
category     | field | sorder | strict
------------ | ----- | ------ | ------
all          | size  |  asc   | -1 *(fuzzy)*
movies       | files |  desc  | 1  *(strict)*
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
   "info":{  
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
- [x] Strict Search
- [x] Fuzzy Search
- [ ] Subtract Words
- [ ] Certain Uploader
- [ ] Safety Filter
- [ ] Only Verified Torrents

Licence
====
Open sourced under [MIT License](LICENSE)
