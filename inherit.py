#!/usr/bin/env python3


class SchoolMember:
	'''Представляет любого человека в школе.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Created SchoolMember: {0})'.format(self.name))

	def tell(self):
		'''Вывести информацию.'''
		print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
	"""docstring for Teacher"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Created Teacher: {0})'.format(self.name))
		
	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
	"""docstring for Student"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Created Student: {0})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
	member.tell()
	