#!/usr/bin/env python3


def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input('Enter text: ')
if (is_palindrome(something)):
	print('Yes, it\'s palindrome')
else:
	print('No, it isn\'t palindrome')
