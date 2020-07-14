# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:40:20 2020

@author: Manjunath GS
"""


import random
import string
from faker import Faker


fake=Faker()

class dataGenerator:
    def __init__(self):
        self.values=[]
        
    def random_decimal_gen(self,column,rec_count):
        self.values.clear()
        if '.' in column[1]:
            digit_len=int(column[1].split('.')[0])
            range_start=10**(digit_len-1)
            range_end=(10**digit_len)-1
            for _ in range(rec_count):
                self.values.append((random.randint(range_start,range_end))/100)
        else:
            digit_len=int(column[1])
            range_start=10**(digit_len-1)
            range_end=(10**digit_len)-1
            for _ in range(rec_count):
                self.values.append(random.randint(range_start, range_end))
        return self.values
    
    def random_string_gen(self,column,rec_count):
        self.values.clear()
        digit_len=int(column[1])
        for _ in range(rec_count):
            if(digit_len < 5):
                letters=string.ascii_uppercase
                res_str=''.join(random.choice(letters) for i in range(digit_len))
                self.values.append(res_str)
            else :
                self.values.append((fake.text(max_nb_chars=digit_len)))
        return self.values
    
    def random_date_gen(self,rec_count):
        self.values.clear()
        for _ in range(rec_count):
            self.values.append(fake.date('%Y-%m-%d'))
        return self.values
    
    def random_name_gen(self,rec_count):
        self.values.clear()
        for _ in range(rec_count):
            self.values.append(fake.name())
        return self.values
    
    def random_address_gen(self,rec_count):
        self.values.clear()
        for _ in range(rec_count):
            self.values.append(fake.address())
        return self.values