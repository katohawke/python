#!/usr/bin/env python3

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# 2. Резервные копии должны храниться в основном каталоге резерва.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# 5. Будем использовать стандартную команду 7z
# стандартном дистрибутиве GNU/Linux. Пользователи Windows могут установить её
# Обратите внимание, что для этого подойдёт любая команда
# архивации, если у неё есть интерфейс командной строки, чтобы ей можно было
# передавать аргументы из нашего сценария.

import sys
import os
import time

line = sys.argv
while line:
	# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
	source = []
	if len(line) == 1 or len(line) == 0:
		print('Usage backup_ver1.py <arguments>')
		break
	else:
		del sys.argv[0]
	for path in line:
		source.append(path)

	# 2. Резервные копии должны храниться в основном каталоге резерва.
	target_dir = 'D:\\Backup' # Подставьте тот путь, который вы будете использовать.

	# 3. Файлы помещаются в zip-архив.
	# 4. Именем для zip-архива служит текущая дата и время.
	target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

	path_command = 'c: && cd "c:\\Program files\\7-zip"'
	
	string = input('Do you want to set password? (Y or N): ')
	#  5. Используем команду "7z" для помещения файлов в zip-архив
	#  Установливаем пароль если нужно
	if string.upper() == 'Y':
		password = input('Enter password: ')
		password = '-p' + password
	else:
		password = ''

	zip_command = path_command + " && " + "7z a -tzip {password} {0} {1}".format(target, ' '.join(source), password=password)		
	# Запускаем создание резервной копии

	if os.system(zip_command) == 0:
		print('Резервная копия успешно создана в', target)
		break
	else:
		print('Создание резервной копии НЕ УДАЛОСЬ')
		break