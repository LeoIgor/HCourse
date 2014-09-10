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
		
	phone_book.sort()
	
	return phone_book
	
def get_name(phone):
	phone_book = read_phone_book_to_dict()
	
	return phone_book.get(str(phone), "Not found")


if __name__ == "__main__":
	print(get_name(5004360))
