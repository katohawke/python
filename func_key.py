#!/usr/bin/env python3


def func(a, b=5, c=10):
	print('a equals to', a, ', b equals to', b, ', and c equals to', c)

func(3, 7)
func(255, c=24)
func(c=50, a=100)
