#!/usr/bin/env python3


shoplist = ['apples', 'mango', 'carrot', 'bananas']
name = 'swaroop'

for elem in range(len(shoplist)):
	print('Element {elem} -'.format(elem=elem), shoplist[elem])

for elem in range(-1, -len(shoplist), -1):
	print('Element {elem} -'.format(elem=elem), shoplist[elem])

for char in range(len(name)):
	print('Symbol {char} -'.format(char=char), name[char])

print('ELements from 1 to 3 -', shoplist[1:3])
print('Elements from 2 to end -', shoplist[2:])
print('ELements from 1 to -1 -', shoplist[1:-1])
print('Elements from start to end -', shoplist[:])
print('Symbols from 1 to 3 -', name[1:3])
print('Symbols from 2 to end -', name[2:])
print('Symbols from 1 to -1 -', name[1:-1])
print('Symbols from start to end -', name[:])
