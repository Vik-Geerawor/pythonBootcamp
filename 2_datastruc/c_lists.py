def basics():
    # declare and init a list
    mylist = [1, 'two', 3]

    # display the list
    print(f"My list: {mylist}")

    # indexing
    print(f"Item no. 2: {(mylist[1])}")

    # slicing
    print(f"Items starting from 2nd item: {(mylist[1:])}")

    # concatenate
    list2 = [4, 5]
    mynewlist = mylist + list2
    print(f"My new list: {mynewlist}")

    # append
    mynewlist.append(7)
    print(f"My list after pending 7: {mynewlist}")

    # pop
    mynewlist.pop(1)
    print(f"My list after popping out 2nd item: {mynewlist}")
    mynewlist.pop()     # default index = -1
    print(f"My list after popping out the last item: {mynewlist}")

    # insert
    mynewlist.insert(1, 2)
    print(f"My list after insert 2 in 2nd position: {mynewlist}")

    # sort
    myshoppinglist = ['milk', 'eggs', 'toast', 'apple', 'banana']
    print(f"\nMy shopping list: {myshoppinglist}")
    myshoppinglist.sort()
    print(f"My sorted shopping list: {myshoppinglist}")

    # reverse
    myshoppinglist.reverse()
    print(f"My reverse-sorted shopping list: {myshoppinglist}")


if __name__ == '__main__':
    print("\n*** LISTS ***")

    basics()
