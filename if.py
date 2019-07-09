#!/usr/bin/env python3

number = 23
guess = int(input('Enter integer number: '))

if guess == number:
    print('Congratulations, you guessed it,')
    print('(although not won any prize!)')
elif guess < number:
    print('No, the hidden number is a little more than that.')
else:
    print('No, the hidden number is a little less than that.')

print('Completed')