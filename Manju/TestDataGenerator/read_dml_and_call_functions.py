# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:26:13 2020

@author: Manjunath GS
"""
from TestDataGenerator import dataGenerator
import numpy as np
import pandas as pd
import re

source_file="C:/Users/home/TestDataGenerator/sample_abinitio.dml"
target_op_file="C:/Users/home/TestDataGenerator/output_data_file.csv"
dtype_list=[]
col_list=[]
n=10 #no of records
col_values=[]
with open(source_file) as fl:
    txt=fl.readlines()
    counter=len(txt)
   

with open(source_file) as fh: 
    fh.readline()
    for i in range(1,counter-1):
        words=str.split(fh.readline())
        dtype_list.append(words[0])
        col_list.append(words[1])

#print(dtype_list)
#print(col_list)

temp_arr=np.zeros((n,0),int)
#print(temp_arr)


for i in dtype_list:
    if i[0:3]=='dec':
            char_len=re.search('\(([0-9]+)\)', i).group(1)
            col_values.append(dataGenerator.random_int_gen(int(char_len), n))
                   
    elif i[0:3]=='str':
            char_len=re.search('\(([0-9]+)\)', i).group(1)
            col_values.append(dataGenerator.random_str_gen(int(char_len), n))
            
    elif i[0:3]=='dat':
        col_values.append(dataGenerator.random_date_gen(n))
        
temp_arr=np.column_stack(col_values)
#print(temp_arr)

df=pd.DataFrame(temp_arr,columns=col_list)
print(df)
df.to_csv(target_op_file,index=False)

        
        


