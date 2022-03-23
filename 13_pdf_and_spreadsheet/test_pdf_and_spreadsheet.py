import PyPDF2
import csv
import re


def get_url(filename):
    with open(filename, encoding='utf-8') as file:
        csv_file = csv.reader(file)
        rows = list(csv_file)

        url = []
        i = 0
        for row in rows:
            url.append(row[i])
            i += 1

        return ''.join(url)


def get_tel_number(filename):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        print(type(reader.getPage(0)))
        # print(reader.getPage(0).extractText())
        for page in reader.pages:
            tel = re.search(r'\d{3}.\d{3}.\d{4}', page.extractText())
            if tel is not None:
                break

    return tel.group()


if __name__ == '__main__':
    print(f"*** PDF and Spreadsheet Test ***")

    my_file = 'find_the_link.csv'
    url = get_url(my_file)
    print(url)

    # get_pdf_from_url(url)
    my_file = 'Find_the_Phone_Number.pdf'
    tel = get_tel_number(my_file)
    print(tel)


