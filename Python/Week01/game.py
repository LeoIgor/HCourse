# -*- coding: utf-8 -*-

from random import randint

MIN_VALUE = 1
MAX_VALUE = 100

def game():
	guess_num = randint(MIN_VALUE,MAX_VALUE)
	count = 0
	
	while True:
		x = input("num: ")
		count += 1

		if x.isdigit():
			x = int(x)

			if x == guess_num:
				print("Число угадано. Количество попыток: %s" % count)
				break
			elif guess_num > x:
				print(":(\n>")
			elif guess_num < x:
				print(":(\n<")		
		else:
			print("Введите целое число.")

if __name__ == "__main__":
	game()
