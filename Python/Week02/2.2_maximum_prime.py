# -*- coding: utf-8 -*-

def maximum_prime(n):
	result = n
	
	while n > 2:
		n -= 1
		if result % n == 0: result = n
		
	return result
	
if __name__ == "__main__":
	print(maximum_prime(70))
