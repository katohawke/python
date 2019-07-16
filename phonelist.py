#!/usr/bin/env python3

# Телефонная книга 

import pickle


class PhoneList:

	phonelist = {}
	phonelistfile = 'phonelist.data'
	temporary = {}

	def __init__(self, name, phone):
		'''Инициализация'''
		self.name = name
		self.phone = phone
		PhoneList.phonelist[name] = phone
		print('Успешно добавлен.')

	@staticmethod
	def show():
		'''Показать всю телефонную книгу'''

		try:
			PhoneList.open(PhoneList.temporary)
			if len(PhoneList.temporary) != 0: 
				print('Имя | Телефон')
				for person in PhoneList.temporary:
					print('{person}: {phone}'.format(person=person, phone=PhoneList.temporary[person]))
			else:
				print('Телефонная книга пуста.')	
		except EOFError:
			print('Телефонная книга пуста.')

	@staticmethod
	def open(namelist):
		with open(PhoneList.phonelistfile, 'rb') as f:
			namelist.update(pickle.load(f))		

	@staticmethod
	def add():
		with open(PhoneList.phonelistfile, 'wb') as f:
			pickle.dump(PhoneList.phonelist, f)

		PhoneList.open(PhoneList.temporary)

		PhoneList.save(PhoneList.temporary)

	@staticmethod
	def save(namelist):
		with open(PhoneList.phonelistfile, 'wb') as f:
			pickle.dump(namelist, f)		

	@staticmethod
	def change(name, phone):
		PhoneList.open(PhoneList.temporary)
		if name in PhoneList.temporary:
			print('Контактные данные успешно изменены.')
			PhoneList.temporary[name] = phone
			PhoneList.save(PhoneList.temporary)
			print('Успешно изменен.')
		else:
			print('Ошибка данных.')	

	@staticmethod
	def delete(name):
		try:
			PhoneList.open(PhoneList.temporary)
			del PhoneList.temporary[name]
			PhoneList.save(PhoneList.temporary)			
			print('Успешно удален.')
		except EOFError:
			print('Телефонная книга пуста. Нечего удалять.')
		except KeyError:
			print('Вы не ввели имя.')

	@staticmethod
	def find(data):
		PhoneList.open(PhoneList.temporary)
		if data in PhoneList.temporary:
			name = data
			phone = PhoneList.temporary[name]
			print('Найдено {0}: {1}.'.format(name, phone))
		elif data in PhoneList.temporary.values():
			phone = data
			name = PhoneList.__key_with_value(phone, default='') 
			print('Найдено {0}: {1}.'.format(name, phone))
		else:
			print('Не найдено.')

	@staticmethod
	def __key_with_value(value, default=None):
		PhoneList.open(PhoneList.temporary)
		for key, value in PhoneList.temporary.items():
			if value == value:
				return key
		return default


def format_personal_info(text):
	personal_info = input(text)
	personal = personal_info.split(' ')
	new_list = []
	for i in range(len(personal)):
		try:
			number = int(personal[i])
			del personal[i]
			new_list.append(number)
		except ValueError:
			continue
	new_list.append(' '.join(personal))
	return new_list


def main():
	while True:
		line = input('''add - добаить контактные данные
delete - удалить контактные данные
change - изменить контактные данные
find - найти контакные данные
show - показать телефонную книгу
exit - выйти \n''')
		print()
		if line:
			choice = line
			if choice.lower() == 'add':
				personal = format_personal_info('Введите контактные данные (имя и номер): ')
				try:
					PhoneList(personal[1], personal[0])
				except IndexError:
					print('Вы не ввели данные.')
				PhoneList.add()
			
			elif choice.lower() == 'delete':
				personal_info = input('Введите имя для удаления: ')
				PhoneList.delete(personal_info)
			
			elif choice.lower() == 'change':
				personal = format_personal_info('Введите контактные данные для изменения (имя и номер): ')
				PhoneList.change(personal[0], personal[1])
			
			elif choice.lower() == 'find':
				personal_info = input('Введите имя или номер для поиска: ')
				PhoneList.find(personal_info)
			elif choice.lower() == 'show':
				PhoneList.show()
			elif choice.lower() == 'exit':
				print('Вы успешно вышли.')
				break
			else:
				print('Не правильная команда.')
			print()
		else:
			break


if __name__ == '__main__':
	main()
