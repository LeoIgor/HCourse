# -*- coding: utf-8 -*-

from bisect import bisect_left

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

def get_name_from_sorted_tuples_list(phone):
    phone_book = read_phone_book_to_sorted_tuples_list()
    phone = str(phone)
    
    index = bisect_left([i[0] for i in phone_book], phone)
    
    if phone_book[index][0] == phone:
        return phone_book[index][1]
    else:
        return "Not found"
    
    
if __name__ == "__main__":
	print(get_name_from_sorted_tuples_list(1010313))
