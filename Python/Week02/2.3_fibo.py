# -*- coding: utf-8 -*-

"""
Числа Фибоначчи — элементы числовой последовательности
в которой каждое последующее число равно сумме двух предыдущих чисел. 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
"""

COUNTER = 0;

def fibo(n):
    global COUNTER 
    COUNTER = COUNTER + 1
    print("=" * 80)
    print("Итерация: " + str(COUNTER))
    
    if n == 0: 
        print("n = 0")
        return 0
    if n == 1: 
        print("n = 1")
        return 1
    
    print(("{0} - 1 = {1}; {2} - 2 = {3}").format(str(n), str(n-1), str(n), str(n-2)))
    
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    print("\nFibo: " + str(fibo(8)))
