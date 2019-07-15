#!/usr/bin/env python3


class ShortInputException(Exception):
	"""docstring for ShortInputException"""
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast


try:
	text = input('Enter something  --> ')
	if len(text) < 3:
		raise ShortInputException(len(text), 3)
except EOFError:
	print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
	print('ShortInputException: Длина введённой строки -- {0}; \
			ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
	print('Не было исключений.')
