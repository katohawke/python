#!/usr/bin/env python3


name = 'Swaroop'

if name.startswith('Swa'):
	print('Yes, string starts with \'Swa\'')

if 'a' in name:
	print('Yes, string contains \'a\'')

if name.find('war') != -1:
	print('Yes, string contains \'war\'')

delimeter = '_*_'

mylist = ['Brazilia', 'Russia', 'India', 'China']
print(delimeter.join(mylist))
