#!/usr/bin/env python3


import os
import platform
import logging

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(
		os.getenv('HOMEDRIVE'), 
		os.getenv('HOMEPATH'), 
		'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("Saved log in", logging_file)

logging.basicConfig(
	level=logging.DEBUG, 
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename=logging_file,
	filemode='w',
)

logging.debug('Starting programme')
logging.info('Some acts...')
logging.warning('Programme is dying')