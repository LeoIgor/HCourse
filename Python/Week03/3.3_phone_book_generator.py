# -*- coding: utf-8 -*-

import random
import string

MIN_NAME_LEN = 4            # минимальная длинна  имени
MAX_NAME_LEN = 10           # максимальная длинна имени

MIN_PHONE_NUM = 1000000     # минимально возможный номер телефона
MAX_PHONE_NUM = 9999999     # максимально возможный номер телефона

FILE_NAME = "PhoneBook.txt" # имя выходного файла


def get_random_name():
"""Return random name"""
    name = "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(MIN_NAME_LEN, MAX_NAME_LEN))])
    name = name[0].upper() + name[1:]
    return name

def get_random_number():
"""Return random phone number"""
    return str(random.randint(MIN_PHONE_NUM, MAX_PHONE_NUM))
    
def generate_phone_book(items_count):
    nums = []
    
    for i in range(1,items_count+1):
        phone_num = get_random_number()
        # соблюдаем требование уникальности телефонных номеров
        while phone_num in nums:
            phone_num = get_random_number()
        nums.append(phone_num)
        
    f = open(FILE_NAME, 'w')
    for num in nums:
        f.write("{0}:{1}\n".format(num, get_random_name()))
    f.close()


if __name__ == "__main__":
    generate_phone_book(100000)
