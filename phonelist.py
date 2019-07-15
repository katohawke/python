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
		
	def open(namelist):
		with open(PhoneList.phonelistfile, 'rb') as f:
			namelist.update(pickle.load(f))		

	def add():
		with open(PhoneList.phonelistfile, 'wb') as f:
			pickle.dump(PhoneList.phonelist, f)

		PhoneList.open(PhoneList.temporary)

		PhoneList.save(PhoneList.temporary)

	def save(namelist):
		with open(PhoneList.phonelistfile, 'wb') as f:
			pickle.dump(namelist, f)		

	def change(name, phone):
		PhoneList.open(PhoneList.temporary)
		if name in PhoneList.temporary:
			print('Контактные данные успешно изменены.')
			PhoneList.temporary[name] = phone
			PhoneList.save(PhoneList.temporary)
			print('Успешно изменен.')
		else:
			print('Ошибка данных.')	

	def delete(name):
		try:
			PhoneList.open(PhoneList.temporary)
			del PhoneList.temporary[name]
			PhoneList.save(PhoneList.temporary)			
			print('Успешно удален.')
		except EOFError:
			print('Телефонная книга пуста. Нечего удалять.')

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

	def __key_with_value(value, default=None):
		PhoneList.open(PhoneList.temporary)
		for key, value in PhoneList.temporary.items():
			if value == value:
				return key
		return default


def main():
	while True:
		line = input('''add - добаить контактные данные
delete - удалить контактные данные
change - изменить контактные данные
find - найти контакные данные
show - показать телефонную книгу\n''')
		print()
		if line:
			choice = line
			if choice.lower() == 'add':
				personal_info = input('Введите контактные данные (имя и номер): ')
				personal = personal_info.split(' ')
				person = PhoneList(personal[0], personal[1])
				PhoneList.add()
			
			elif choice.lower() == 'delete':
				personal_info = input('Введите имя для удаления: ')
				PhoneList.delete(personal_info)
			
			elif choice.lower() == 'change':
				personal_info = input('Введите контактные данные для изменения (имя и номер): ')
				personal = personal_info.split(' ')
				PhoneList.change(personal[0], personal[1])
			
			elif choice.lower() == 'find':
				personal_info = input('Введите имя или номер для поиска: ')
				PhoneList.find(personal_info)
			
			elif choice.lower() == 'show':
				PhoneList.show()
			print()
		else:
			break


if __name__ == '__main__':
	main()