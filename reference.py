#!/usr/bin/env python3


print('Simple =')
shoplist = ['appples', 'mango', 'carrot', 'bananas']
mylist = shoplist
del shoplist[0]

print('shoplist: ', shoplist)
print('mylist: ', mylist)


print('Copy with usage full cuting: ')
mylist = shoplist[:]
del mylist[0]
		
print('shoplist: ', shoplist)
print('mylist: ', mylist)
