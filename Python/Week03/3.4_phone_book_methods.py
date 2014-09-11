# -*- coding: utf-8 -*-

from bisect import bisect_left
import time

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
        
        
"""
>Сравните скорость поиска в трёх случаях (придумайте сами методику, 
по которой можно сравнить скорость).

1. Поиск заведомо отсутствующего значения   5000000
2. Поиск значения в начале списка           4580468
3. Поиск значения в конце списка            2777083
4. Поиск значения в середине списка         3123503

Бенчмарк заведомо несколько некорректный т.к. в функции бинарного поиска
каждую итерацию выполняется сортировка списка.
"""
def func_testing(func_name):
    
    test_data = {5000000 : "Поиск заведомо отсутствующего значения",
                 4580468 : "Поиск значения в начале списка",
                 2777083 : "Поиск значения в конце списка",
                 3123503 : "Поиск значения в середине списка"}
    
    t1 = time.clock()
    t2 = 0
    
    print("{0}:\n{1}".format(func_name.__name__, "=" * 80))
    
    for phone in test_data.keys():
        i = 1
        while i <= 100:
            func_name(phone)
            i += 1
            
        t2 = time.clock() - t1
        print("{0}: {1}".format(test_data[phone], t2))
        t1 = time.clock()
        
    print()

"""
Печальный результат:

get_name_from_dict:
================================================================================
Поиск заведомо отсутствующего значения: 8.421644679759742
Поиск значения в конце списка: 8.405817222650986
Поиск значения в начале списка: 8.408951375539885
Поиск значения в середине списка: 8.417067336500342

get_name_from_tuples_list:
================================================================================
Поиск заведомо отсутствующего значения: 10.89795442670259
Поиск значения в конце списка: 10.757366053238357
Поиск значения в начале списка: 10.043180663346256
Поиск значения в середине списка: 10.404103789865246

get_name_from_sorted_tuples_list:
================================================================================
Поиск заведомо отсутствующего значения: 26.81808910449692
Поиск значения в конце списка: 26.885584993936007
Поиск значения в начале списка: 26.929659973922497
Поиск значения в середине списка: 26.97807561035239
"""

if __name__ == "__main__":
    func_testing(get_name_from_dict)
    func_testing(get_name_from_tuples_list)
    func_testing(get_name_from_sorted_tuples_list)
