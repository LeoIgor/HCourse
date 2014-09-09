# -*- coding: utf-8 -*-

"""
Проверка аргумента с помощью isdigit() + допущения:
 - Число может быть отрицательным
 - Число может не быть целым (разделитель - точка)
 - Число может быть отрицательным И не целым
 
 Всё остальное числом не считаем

"""

DEC_SEPARATOR = '.' # Десятичный разделитель

"""
Является ли x беззнаковым float?
Вынес в отдельную функцию для избежания дублирования кода
"""
def is_unsigned_float(x):
    if len(x.split(DEC_SEPARATOR)) == 2:
        a,b = x.split(DEC_SEPARATOR)
        if a.isdigit() and b.isdigit(): return True
    
    return False


def is_number(x):
    if type(x) != str: return False     # Принимаем только str
    if len(x) < 1: return False         # Это точно не число
    if x.isdigit(): return True         # Беззнаковое целое
    if x[0] == "-" and x[1:].isdigit(): # Отрицательное целое
        return True
    
    if is_unsigned_float(x): return True
    if x[0] == "-" and is_unsigned_float(x[1:]): return True
    
    return False # всё отфильтровано, остальное нас не устраивает
  

if __name__ == "__main__":
    print(is_number("-234.12"))
    print(is_number("234.12"))
    print(is_number("234.12.123"))
    print(is_number("-234"))
    print(is_number("234"))
    print(is_number("asd"))
    print(is_number(""))
    print(is_number(2))
    print(is_number(2.13))
    print(is_number(-2))
