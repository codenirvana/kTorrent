import requests, json, __future__
from bs4 import BeautifulSoup

# Base search link
BASE_LINK = 'https://kat.cr/usearch/'

# Error Message if requests method fails to get content
ERROR_MESSAGE = "Couldn't retrieve data"

### Filters to verify passed parameters

# KAT search result fields
FIELD_FILTER = {
    'size'  : 'size',
    'files' : 'files_count',
    'age'   : 'time_add',
    'seed'  : 'seeders',
    'leech' : 'leechers'
}

# Sorting order
SORDER_FILTER = ['asc', 'desc']

# Categories
CATEGORY_FILTER = ['all', 'movies', 'tv', 'anime', 'music', 'books', 'applications', 'xxx']

def search(**args):
#Do a search

    search = args.get('search', '')
    strict = args.get('strict', '0')
    safe = args.get('safe', '0')
    verified = args.get('verified', '0')
    subtract = args.get('subtract', '')
    user = args.get('user', '')
    category = args.get('category', 'all')
    field = args.get('field', 'age')
    sorder = args.get('sorder', 'desc')
    page = args.get('page', '1')

    dict_keys = ['name', 'link', 'magnet', 'verified', 'category', 'size', 'files', 'age', 'seed', 'leech']

    ### Generate Search Query ###
    # Strictness
    if strict == '-1':
        search_query = search.replace(" ", " OR ")
    elif strict == '1':
        search_query = '"' + search + '"'
    else:
        search_query = search

    # Category
    search_query = search_query + ' category:' + category

    # Safety
    if safe == '1':
        search_query = search_query + ' is_safe:1'

    # Verified
    if verified == '1':
        search_query = search_query + ' verified:1'

    # Subtract specified word(s)
    if subtract != '':
        words = subtract.split()
        for word in words:
            search_query = search_query + ' -' + word

    # Uploads by certain user
    if user != '':
        search_query = search_query + ' user:' + user

    ### Generate Final Link ###
    link = BASE_LINK + search_query + '/' + page + '/?field=' + FIELD_FILTER[field] +'&sorder=' + sorder

    try:
        response = requests.get(link)
    except:
        return ERROR_MESSAGE

    soup = BeautifulSoup(response.text,"html.parser")
    rows = soup.select('[id^=torrent_]')
    rows_found = len( rows )

    if rows_found > 0:
        result = []
        for row in rows:
            cols = row.find_all('td')
            links = cols[0].select('.iaconbox a')   # All related links

            # Extracting Torrent information
            name = ( cols[0].select('.cellMainLink') )[0].text
            link = 'http:' + links[-1].get('href')
            magnet = links[-2].get('href')
            category = ( cols[0].select('[id^=cat_]') )[0].text
            # Check if verified
            verified = '0'    # False
            if len(links) > 3:
                if links[-4].get('title') == "Verified Torrent":
                    verified = '1'

            row_data = [ name, link, magnet, verified, category ]

            for i in range(1,6):
                row_data.append(cols[i].text.strip())

            # Zip keys with values
            row_data = zip( dict_keys, list( (x.replace(u'\xa0', u' ')) for x in row_data) )

            # Append current torrent to results
            result.append( dict( row_data ) )

        # Calculate total pages
        pager =  soup.select('.pages a')
        total_pages = 1 if len( pager ) == 0 else pager[ - 1 ].text

        data = {
            'info' : {
                'pageCurrent' : int( page ),
                'pageResult'  : rows_found,
                'pageTotal'   : total_pages
            },
            'torrent' : result
        }
    else:
        data = "Nothing found"

    return json.dumps(data,sort_keys=True)
