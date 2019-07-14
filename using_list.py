#!/usr/bin/env python3


shoplist = ['apples', 'mango', 'carrot', 'bananas']

print('I have to ', len(shoplist), 'buying.')

print('Shoping:', end=' ')
for item in shoplist:
	print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('Now my shoplist like :', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)
