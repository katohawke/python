#!/usr/bin/env python3

x = 50


def func(x):
    print('x is equal to {} .'.format(x))
    x = 2
    print('Замена локального x на {}.'.format(x))

func(x)
print('x по прежнему {} .'.format(x))
