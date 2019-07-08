# !/usr/bin/env python3
# Programme which generates a password with a given length

from random import randint


def generate_password(lgth):

    """
    generate password with length entered
    :param lgth: integer
    :return: string
    """

    string = ''
    # generate choice of number from 1 to 3
    # 1: 49-57 generate number from 0 to 9
    # 2: 65-90 generate uppercase letter
    # 3: 97-122 generate lowercase letter
    while lgth > 0:
        choice = randint(1, 3)
        if choice == 1:
            char = chr(randint(49, 57))
        elif choice == 2:
            char = chr(randint(65, 90))
        else:
            char = chr(randint(97, 122))

        string += char
        lgth -= 1

    return string


if __name__ == '__main__':

    line = input('Enter the length: ')

    try:
        length = int(line)
        password = generate_password(length)
        print(password)
    except ValueError:
        print('Length must be integer.')