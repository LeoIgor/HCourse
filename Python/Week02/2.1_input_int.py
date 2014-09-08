# -*- coding: utf-8 -*-

def input_int(a,b):
    while True:
        x = input("num: ")
        if x.isdigit() and int(x) in range(a,b+1): return x
        else:
            print("try again")

if __name__ == "__main__":
    input_int(1,100)
