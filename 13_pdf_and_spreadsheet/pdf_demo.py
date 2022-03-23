import PyPDF2


def read_pdf(filename):
    # open file as binary for reading
    with open(filename, 'rb') as file:
        # create reader from file
        pdf_reader = PyPDF2.PdfFileReader(file)

        # print number of pages in file
        print(pdf_reader.numPages)

        # grab page 1
        page_one = pdf_reader.getPage(0)

        # get the content of the page
        page_one_text = page_one.extractText()

        # show the content of page 1
        print(page_one_text)


def save_first_page(in_f, out_f):
    # open file as binary for reading
    with open(in_f, 'rb') as in_f, open(out_f, 'wb') as out_f:

        # create reader object from input file
        pdf_reader = PyPDF2.PdfFileReader(in_f)
        # get the page object to copy
        a_page = pdf_reader.getPage(0)

        # create writer object
        pdf_writer = PyPDF2.PdfFileWriter()     # TODO: does not any arg
        # add a page object to writer
        pdf_writer.addPage(a_page)
        # write to output file
        pdf_writer.write(out_f)


if __name__ == '__main__':
    print(f"*** PDF Demo ***")

    # my_filename = 'dental_policy.pdf'
    # page = read_pdf(my_filename)

    in_file = 'dental_policy.pdf'
    out_file = 'result.pdf'
    lorem_ipsum = '''
    Lorem ipsum dolor sit amet. Ut eveniet ullam et quia nemo et voluptatum 
    dolores! Aut ipsum commodi eos magni ducimus sed culpa delectus cum 
    voluptatem laboriosam sed nisi quisquam et internos facilis. Aut rerum 
    consequatur ut sint aspernatur est soluta explicabo est magnam officiis?\n
    Aut cupiditate veniam sit laudantium quis ut doloremque tempora sit laudantium 
    rerum. Ut voluptatem odio est veniam atque ut repellendus culpa eum quidem 
    optio qui cumque alias cum rerum ducimus ut dolorem aperiam?\n
    Vel repellat vitae eum nobis quis sed sequi eligendi eos internos error 33 
    dolorem architecto! Ex illo quae quo molestias molestias ab reiciendis nihil.
    '''

    save_first_page(in_file, out_file)
