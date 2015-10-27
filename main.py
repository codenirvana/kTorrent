import requests, bs4, click, __future__, sys, urllib2
from pprint import pprint

all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'

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
    search = raw_input("Search For: ")
    #search = args.get('search', '')
    category = args.get('category', 'all')
    field = args.get('field', 'age')
    sorder = args.get('sorder', 'desc')
    page = args.get('page', '1')

    dict_keys = ['name', 'link', 'category', 'size', 'files', 'age', 'seed', 'leech']

    search_query = search + ' category:' + category
    link = base_link + search_query + '/' + page + '/?field=' + field_filter[field] +'&sorder=' + sorder

    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    rows = soup.select('[id^=torrent_]')

    data = []
    for row in rows:
        cols = row.find_all('td')
        name = cols[0].select('.cellMainLink')
        link = cols[0].select('.iaconbox a')
        category = cols[0].select('[id^=cat_]')
        row_data = [ name[0].text, 'http:' + link[-1].get('href'), category[0].text]
        for i in xrange(1,6):
            row_data.append(cols[i].text.strip())
        data.append( dict(zip( dict_keys, list( (x.replace(u'\xa0', u' ')).encode('ascii', 'ignore')  for x in row_data) )) )

    return data


def download(url):
    rq = urllib2.Request(url)
    res = urllib2.urlopen(rq)
    f = open( (url.split(']'))[1] , 'w')
    f.write(res.read())
    f.close()

@click.command()
@click.option('-c', '--cat', 'category', default='all', help='Torrent Category')
@click.option('-f', '--field', 'field', default='seed', help='Select field to sort')
@click.option('-s', '--sort', 'sorder', default='desc', help='Select Sorting Order')
@click.option('-p', '--page', 'page', default='1', help='Page')
def main(category, field, sorder, page):
    '''
        Let's search a torrent
    '''

    data = get_data(category=category, field=field, sorder=sorder, page=page)
    sys.stdout.flush()
    pprint(data)

    #download(data[0]['link'])

if __name__ == "__main__": main()

# click.echo(click.style('I am colored %s' % color, fg=color))
# click.echo(click.style('I am colored %s and bold' % color, fg=color, bold=True))
# click.echo(click.style('I am reverse colored %s' % color, fg=color, reverse=True))
# click.echo(click.style('I am blinking', blink=True))
# click.echo(click.style('I am underlined', underline=True))
