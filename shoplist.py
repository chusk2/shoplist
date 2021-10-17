# TODO use iterdir to dir content of directory

def create_list(filename):
    with open(f'{filename}.txt', 'w') as file:

        while True:
            new_item = input('Add item: ')
            if new_item:
                file.write(new_item)
            else:
                break


def add_items(filename):
    with open(f'{filename}.txt', 'a') as file:
        while True:
            new_item = input('Add item to list: ')
            if new_item:
                file.write(new_item)
            else:
                break


def read_list(filename):

    with open(f'{filename}.txt', 'r') as f:
        # f is an iterable
        for line in f:
            # rstrip(str) : removes str from right end of string
            print(line.rstrip('\n'))

option = input('Create (c), add items (a), read (r): ')

while True:
    if option == 'c':
        filename = input('Filename: ')
        create_list(filename)
    elif option == 'a':
        filename = input('Filename: ')
        add_items(filename)
    elif option == 'r':
        filename = input('Filename: ')
        read_list(filename)
    else:
        break