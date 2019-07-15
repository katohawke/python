#!/usr/bin/env python3


try:
	text = input('Enter something --> ')
except EOFError:
	print('Why did you do EOF me ?')
except KeyboardInterrupt:
	print('You escaped operation.')
else:
	print('You entered {text}'.format(text=text))