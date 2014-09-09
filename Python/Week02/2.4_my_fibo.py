# -*- coding: utf-8 -*-

def myfibo(n):
    num1 = 0
    num2 = 1
    
    counter = 1
    
    while(counter != n):
        num1, num2 = num2, num1 + num2
        counter += 1
        
    return num2
        

if __name__ == "__main__":
    print(myfibo(10))
