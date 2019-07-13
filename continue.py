#!/usr/bin/env python3

while True:
    s = input('Enter something: ')
    if s.lower() == 'exit':
        break
    if len(s) < 3:
        print('Too little...')
    continue
    print('The entered string is of sufficient length!')
