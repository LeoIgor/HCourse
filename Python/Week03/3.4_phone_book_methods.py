# -*- coding: utf-8 -*-

"""
Задание 3.4. Прочитайте вашу телефонную книгу из файла:

Для упорядоченного списка придумайте эффективный метод 
поиска. Сравните скорость поиска в трёх случаях 
(придумайте сами методику, по которой можно сравнить скорость).
"""

FILE_NAME = "PhoneBook.txt"

def read_phone_book_to_dict():
	phone_book = {}
	
	for line in open(FILE_NAME):
		phone, name = line.rstrip().split(":")
		phone_book[phone] = name
		
	return phone_book
		
def read_phone_book_to_tuples_list():
	phone_book = []
	
	for line in open(FILE_NAME):
		phone_book.append(tuple(line.rstrip().split(":")))
	
	return phone_book
		
def read_phone_book_to_sorted_tuples_list():
	phone_book = []
	
	for line in open(FILE_NAME):
		phone_book.append(tuple(line.rstrip().split(":")))
		
	return phone_book.sort()
	
def get_name_from_dict(phone):
	phone_book = read_phone_book_to_dict()
	
	return phone_book.get(str(phone), "Not found")
	
def get_name_from_tuples_list(phone):
	phone_book = read_phone_book_to_tuples_list()
	
	phone = str(phone)
	
	for item in phone_book:
		if phone in item:
			return item[1]
			
	return "Not found"

"""
> придумайте эффективный метод поиска
Нагуглил бинарный поиск, его и попытаюсь реализовать (думаю, на данном этапе 
ничего сложнее и не требуется).
"""	
def get_name_from_sorted_tuples_list(phone):
	pass
	

if __name__ == "__main__":
	get_name_from_sorted_tuples_list(phone)	
