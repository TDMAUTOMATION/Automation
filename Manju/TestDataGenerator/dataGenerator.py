# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:40:20 2020

@author: Manjunath GS
"""


import random
from faker import Faker

fake=Faker()

def random_int_gen(c,n):
    range_start=10**(c-1)
    range_end=(10**c)-1
    res_list=[]
    for i in range(1,n+1):                
        res_list.append(random.randint(range_start, range_end))
    return res_list

def random_str_gen(c,n):
    res_list=[]
    for i in range(1,n+1):
        if(c < 5):
            res_list.append('NA')
        else :
            res_list.append((fake.text(max_nb_chars=c)))
    return res_list

def random_date_gen(n):
    res_list=[]
    for i in range(1,n+1):
        res_list.append(fake.date('%m%d%Y'))
    return res_list
    