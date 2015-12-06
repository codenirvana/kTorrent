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
search = ktorrent.search(search='linux', category='books', field='age', sorder='desc', page='2')
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

Licence
====
Open sourced under [MIT License](LICENSE)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/codenirvana/ktorrent/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

