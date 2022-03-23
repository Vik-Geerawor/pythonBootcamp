import requests
import lxml
import bs4


def grab_title(a_url):
    # get html text
    html = requests.get(a_url)
    # print(title.text)

    # parse using BeautifulSoup
    bs = bs4.BeautifulSoup(html.text, 'lxml')
    # print(bs)

    # select the tag needed
    titles = bs.select('title')
    # print(f"List of titles: {titles}")

    # select one element from the list with the same tag
    first_title = titles[0]
    # print(f"First title: {first_title}")

    # get the text of that individual tag
    first_title_text = first_title.getText()
    # print(f"Text of first title: {first_title_text}")

    return first_title_text


def grab_toc(a_url):
    html = requests.get(a_url)
    bs = bs4.BeautifulSoup(html.text, 'lxml')
    toc = bs.select('.toctext')       # <span class="toctext">Career</span>

    return toc


def grab_image(a_url):
    html = requests.get(a_url)
    bs = bs4.BeautifulSoup(html.text, 'lxml')
    images = bs.select('img')

    return images


if __name__ == '__main__':
    print(f"*** Web Scraping ***")
    # title = grab_title('http://www.example.com')
    # print(title)
    #
    # for item in grab_toc('https://en.wikipedia.org/wiki/Grace_Hopper'):
    #     print(f"{item.getText()}")

    images = grab_image('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
    for img in images:
        if 'Deep_Blue' in img['src']:
            img_link = requests.get('https:' + img['src'])
            # print(img_link.url)
            with open(img_link.url.rsplit('/')[-1], 'wb') as f:
                f.write(img_link.content)
                print(f"{img_link.url.rsplit('/')[-1]} saved")
