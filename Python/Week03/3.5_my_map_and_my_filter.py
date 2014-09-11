# -*- coding: utf-8 -*-

def my_map(func_name, iterable_obj):
    res = []
    
    [res.append(func_name(x)) for x in iterable_obj]
    
    return res

def my_filter(func_name, iterable_obj):
    res = []
    
    for x in iterable_obj:
        if func_name != None:
            if func_name(x):
                res.append(x)
        else:
            if not x:
                res.append(x)
            
    return res
    

if __name__ == "__main__":
    pass
