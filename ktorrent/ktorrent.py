import requests, json, __future__
from bs4 import BeautifulSoup

BASE_LINK = 'https://kat.cr/usearch/'

ERROR_MESSAGE = "Couldn't retrieve data."

FIELD_FILTER = {
    'size'  : 'size',
    'files' : 'files_count',
    'age'   : 'time_add',
    'seed'  : 'seeders',
    'leech' : 'leechers'
}
SORDER_FILTER = ['asc', 'desc']
CATEGORY_FILTER = ['all', 'movies', 'tv', 'anime', 'music', 'books', 'applications', 'xxx']

def search(**args):
    search = args.get('search', '')
    category = args.get('category', 'all')
    field = args.get('field', 'age')
    sorder = args.get('sorder', 'desc')
    page = args.get('page', '1')

    dict_keys = ['name', 'link', 'category', 'size', 'files', 'age', 'seed', 'leech']

    search_query = search + ' category:' + category
    link = BASE_LINK + search_query + '/' + page + '/?field=' + FIELD_FILTER[field] +'&sorder=' + sorder

    try:
        response = requests.get(link)
    except:
        return ERROR_MESSAGE

    soup = BeautifulSoup(response.text,"html.parser")
    rows = soup.select('[id^=torrent_]')

    result = []
    for row in rows:
        cols = row.find_all('td')
        name = cols[0].select('.cellMainLink')
        link = cols[0].select('.iaconbox a')
        category = cols[0].select('[id^=cat_]')
        row_data = [ name[0].text, 'http:' + link[-1].get('href'), category[0].text]
        for i in range(1,6):
            row_data.append(cols[i].text.strip())
        result.append( dict(zip( dict_keys, list( (x.replace(u'\xa0', u' ')) for x in row_data) )) )

    data = {
        'torrent' : result
    }

    return json.dumps(data)
