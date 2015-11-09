import requests, bs4, click, __future__

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

def colors():
  enums = dict(
    COUNT   = 'white',
    NAME    = 'yellow',
    SEED    = 'green',
    LEECH   = 'red',
    SIZE    = 'cyan',
    AGE     = 'blue'
  )
  return type('Enum', (), enums)

def cap(s, l):
    return s if len(s)<=l else s[0:l-3]+'...'


def get_data(**args):
    search = args.get('search', '')
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

def print_data(data):
    count = 0

    click.secho("%-3s  %-60s    %-20s    %-20s    %s  " % ("#", "NAME", "AGE", "SIZE", "SEEDS"), bold=True, fg="white", reverse=True)

    for torrent in data:
        count += 1
        name = torrent['name']
        age = torrent['age']
        size = torrent['size']
        seed = torrent['seed']
        leech = torrent['leech']

        click.secho("%-3s" % str(count), nl=False, fg=colors().COUNT, bold=True)
        click.secho('  %-60s' % cap(name, 60), nl=False, fg=colors().NAME)
        click.secho('    %-20s' % age, nl=False, fg=colors().AGE)
        click.secho('    %-20s' % size, nl=False, fg=colors().SIZE)
        click.secho('    %s' % seed, nl=False, fg=colors().SEED)
        click.secho(' / ' , nl=False)
        click.secho('%s' % leech, fg=colors().LEECH)


@click.command()
@click.option('-c', '--cat', 'category', default='all', help='Torrent Category')
@click.option('-f', '--field', 'field', default='seed', help='Select field to sort')
@click.option('-s', '--sort', 'sorder', default='desc', help='Select Sorting Order')
@click.option('-p', '--page', 'page', default='1', help='Page')
def main(category, field, sorder, page):
    click.secho("Search For: ", nl=False, fg='white', bold=True)
    search = raw_input()
    try:
        data = get_data(search=search, category=category, field=field, sorder=sorder, page=page)
        print_data(data)
    except:
        print("Error connecting to inrernet")

if __name__ == "__main__": main()
