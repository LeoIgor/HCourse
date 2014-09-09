# -*- coding: utf-8 -*-

import time

def heller_fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return heller_fibo(n - 1) + heller_fibo(n - 2)
    
def my_fibo(n):
    num1 = 0
    num2 = 1
    
    counter = 1
    
    while(counter != n):
        num1, num2 = num2, num1 + num2
        counter += 1
        
    return num2

def compare_functions(f, g, arg):
    i = 0
    t1 = 0
    t2 = 0
    while i < 1000:
        last_time = time.clock()
        f(arg)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(arg)
        t2 += time.clock() - last_time
        i += 1
    print(t2 / t1)


if __name__ == "__main__":
    compare_functions(heller_fibo, my_fibo, 50)
