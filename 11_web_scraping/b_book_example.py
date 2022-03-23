import requests
import bs4


if __name__ == '__main__':
    print(f"*** Example of Scraping ***")

    my_url = 'https://books.toscrape.com/catalogue/page-{}.html'

    for i in range(1, 11):
        # get html page content
        page = requests.get(my_url.format(i))

        # check if valid URL
        if page.ok:
            # display URL
            print(page.url)

            # convert to bs object
            bs = bs4.BeautifulSoup(page.text, 'lxml')

            # grab the right block for further processing
            books = bs.select('.product_pod')

            # for each book on page
            for book in books:
                # check if it book has 3 star rating
                three_star = len(book.select('.star-rating.Three'))     # TODO: replace [space] with "."
                if three_star == 1:
                    # find title of the book
                    title = book.select('h3')[0].select('a')[0]['title']

                    # display title and rating
                    print(f"{title}, Rating: ***")
        else:
            break


