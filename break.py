#!/usr/bin/env python3

while True:
    s = input('Enter something : ')
    if s.lower() == 'exit':
        break

    print('Length of string equals to ', len(s))

print('Completed.')
