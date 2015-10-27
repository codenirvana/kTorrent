import requests, bs4

base_link = 'https://kat.cr/usearch/'

field_filter = {
    'size'  : 'size',
    'files' : 'files_count',
    'age'   : 'time_add',
    'seed'  : 'seeders',
    'leech' : 'leechers'
}

sorder_filter = ('asc', 'desc')

category_filter = ['all', 'movies', 'tv', 'anime', 'music', 'books', 'applications', 'xxx']

def get_data(**args):
    search = args.get('search', '')
    category = args.get('category', 'all')
    field = args.get('field', 'age')
    sorder = args.get('sorder', 'desc')
    page = args.get('page', '1')

    dict_keys = ['name', 'category', 'size', 'files', 'age', 'seed', 'leech']

    search_query = search + ' category:' + category
    link = base_link + search_query + '/' + page + '/?field=' + field_filter[field] +'&sorder=' + sorder

    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    rows = soup.select('[id^=torrent_]')

    data = []
    for row in rows:
        cols = row.find_all('td')
        name = cols[0].select('.cellMainLink')
        category = cols[0].select('[id^=cat_]')
        row_data = [ name[0].text, category[0].text]
        for i in xrange(1,6):
            row_data.append(cols[i].text.strip())
        data.append( dict(zip( dict_keys, list( (x.replace(u'\xa0', u' ')).encode('ascii', 'ignore')  for x in row_data) )) )

    return data


def main():
    data = get_data(search='teamtreehouse',page='2')
    print data


if __name__ == "__main__": main()
