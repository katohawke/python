#!/usr/bin/env python3


class Person:

	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print('Hello! My name is', self.name)

p = Person('Raekan Kato Hawke')
p.sayHi()
