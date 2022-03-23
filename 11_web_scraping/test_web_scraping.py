import requests
import bs4


def get_authors(url):
    page = requests.get(url)
    bs = bs4.BeautifulSoup(page.text, 'lxml')

    authors = bs.select('.author')
    for author in authors:
        print(f"{author.text}")


def get_quotes(url):
    page = requests.get(url)
    bs = bs4.BeautifulSoup(page.text, 'lxml')

    quotes = bs.select('.text')
    for quote in quotes:
        print(f"{quote.text}")


def get_top_10_quotes(url):
    page = requests.get(url)
    bs = bs4.BeautifulSoup(page.text, 'lxml')

    top_10_tags = bs.select('.col-md-4.tags-box')[0].select('a')
    for tag in top_10_tags:
        print(tag.text)


def get_all_authors(url):
    # list of authors
    list_of_authors = []

    # start with first page
    i = 1
    page = requests.get(url.format(i))
    bs = bs4.BeautifulSoup(page.text, 'lxml')
    # check if there is a valid next page
    next_page = bs.select('nav')[0].select('.next')

    while len(next_page) > 0:
        # process current page
        authors = bs.select('.author')
        for author in authors:
            if author.text not in list_of_authors:
                print(f"{page.url}: {author.text}")
                list_of_authors.append(author.text)

        i += 1
        page = requests.get(url.format(i))
        bs = bs4.BeautifulSoup(page.text, 'lxml')
        next_page = bs.select('nav')[0].select('.next')

    return list_of_authors


if __name__ == '__main__':
    print(f"*** Web Scraping Test ***")

    my_url = 'http://quotes.toscrape.com'

    get_authors(my_url)

    get_quotes(my_url)

    get_top_10_quotes(my_url)

    base_url = 'http://quotes.toscrape.com/page/{}/'
    list_of_authors = get_all_authors(base_url)
    list_of_authors.sort()
    print(list_of_authors)



