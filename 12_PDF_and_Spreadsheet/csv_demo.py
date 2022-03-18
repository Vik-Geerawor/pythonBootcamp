import csv


def read_file(filename):
    with open(filename, encoding='utf-8') as data:
        csv_data = csv.reader(data)     # returns an iterable obj, not a list

        # to use index - convert to list
        rows = list(csv_data)
        # print(rows)
        print(f"Row 2: {rows[2]}")

        # get names
        name = []
        data.seek(0)                # reset file read/write position
        for row in csv_data:
            name.append(row[1])
        print(f"Names: {name}")


def write_file(filename, row):
    with open(filename, mode='a', newline='') as data:
        writer = csv.writer(data)
        writer.writerow(row)


if __name__ == '__main__':
    print(f"*** CSV Builtin ***")
    # read_file('data.csv')
    # row = ['4', 'John', '23-Jun-2004']
    # write_file('data.csv', row)


