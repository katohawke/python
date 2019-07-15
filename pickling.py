#!/usr/bin/env python3


import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apples', 'mangoes', 'carrots']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)

print(storedlist)
