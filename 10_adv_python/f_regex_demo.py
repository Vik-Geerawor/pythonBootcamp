import re


def search_one():
    text = "The person's phone number is 408-555-1234. Call on my phone soon!"
    pattern = 'phone'
    print(f"Test: {text}")
    print(f"searching for '{pattern}'")
    result = re.search(pattern, text)
    print(f"\tresult: {result}")
    print(f"\tresult.span: {result.span()}")
    print(f"\tresult.start index: {result.start()}")
    print(f"\tresult.end index + 1: {result.end()}")    # TODO: end = index + 1


def search_all():
    text = "The person's phone number is 408-555-1234. Call on my phone soon!"
    pattern = 'phone'
    print(f"Test: {text}")
    print(f"searching for '{pattern}'")

    phone = re.findall(pattern, text)  # return a list of the pattern itself
    print(f"\tResult: {phone}")

    for i in re.finditer(pattern, text):
        print(f"{i.start()} - {i.end()}")


def regex_one():
    text = "My telephone number is 408-555-1234"
    print(f"text")
    phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
    print(f"\tPhone: \t\t\t{phone}")
    print(f"\tphone.group: \t{phone.group()}")


def regex_two():
    text = "My home tel number is 408-555-1234 and my mob number is " \
           "748-488-4021"
    pattern = r'(\d{3})-(\d{3})-(\d{4})'
    print(f"Text: {text}")
    phone = re.search(r'(\d{3})-(\d{3})-(\d{4})', text)
    print(f"\tPhone: \t\t\t{phone}")
    print(f"Group: {phone.group()}")

    for i in re.finditer(pattern, text):
        print(f"\t{i.group()}: {i.start()} - {i.end()}: Area: {i.group(1)}")


def regex_three():
    text = 'This man was here.'
    pattern = r'man|woman'                  # logical OR
    print(f"'{pattern}' in '{text}'")
    result = re.search(r'man|woman', text)
    print(f"\tresult: {result.span()}")

    text = 'The cat in the hat sat here.'
    pattern = r'...at'                        # at and 3 preceding chars
    print(f"'{pattern}' in '{text}'")
    result = re.findall(r'...at', text)
    print(f"\t{result}")

    pattern = r'\S+at'                        # word ending in
    print(f"'{pattern}' in '{text}'")
    result = re.findall(r'\S+at', text)
    print(f"\t{result}")

    text = 'My name is James, James Bond 007 Secret Agent 3'
    pattern = r'\d{3}'
    print(f"'{pattern}' in '{text}'")
    result = re.findall(r'\d{3}', text)
    print(f"\t{result}")

    text = 'there are 3 numbers 34 inside 5 this sentence.'
    pattern = r'[^\d]+'
    print(f"'{pattern}' in '{text}'")
    result = re.findall(r'[^\d]+', text)        # exclusions with []
    print(f"\t{result}")

    text = 'This is a string! But it has punctuation. How can we remove it?'
    pattern = '[^!.? ]+'
    print(f"'{pattern}' in '{text}'")
    result = re.findall('[^!.? ]+', text)        # exclusions with []
    print(f"\t{' '.join(result)}")

    text = 'Let''s catch some catfish after a catnap'
    pattern = r'cat(fish|nap|food)'
    print(f"'{pattern}' in '{text}'")
    result = re.search(r'cat(fish|nap|food)', text)
    print(f"\tresult: {result.group()}: {result.span()}")


if __name__ == '__main__':
    print(f"*** Regex ***")
    # search_one()
    # search_all()
    # regex_one()
    # regex_two()
    regex_three()
