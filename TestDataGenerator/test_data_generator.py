# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:05:16 2020

@author: Manjunath GS & Jayaprakash M

This module creates a test data as per the specified columns in the abinitio DML.
This modules expects input configuration file which includes below details:
    1-DML file path
    2-DML file name
    3-Output file path
    4-output file name
    5- records count
"""
import sys
import numpy as np
import pandas as pd
import re
from dataGenerator import dataGenerator

class TestDataGenerator():
    #initialize all required variables
    def __init__(self):
        self.input_config=sys.argv[1]
        self.dml_file_name=''
        self.output_file=''
        self.records_count=10
        self.header=[]
        self.columns_name=[]
        self.test_data=[]
        self.temp_arr=[]
    
    def usage(self):
        print('''
              Usage -- test_data_generator.py <input_configuration_file.txt>
              Input configuration file should include below details:
              <DML file path> <DML file name> <Output file path> <output file name> <records count>
              ''')
#argument pass check    
    def argv_check(self,argv):
        if len(sys.argv)!=2:
            print("This python script expects input configuration file as argument.")
            print("Please check and provide the details as :")
            self.usage()
            sys.exit(1)
        
    def input_config_file_validation(self,input_config):
        try:
            with open(self.input_config) as in_txt:
                lines=in_txt.readlines()
                user_input=[]
                if len(lines)!=5:
                    print('Passed input configuration does not contain expected values.')
                    self.usage()
                    sys.exit(2)
                else:
                    for i in lines:
                        user_input.append(i.split('-')[1].strip())  
                    self.dml_file_name=user_input[0]+user_input[1]
                    self.output_file=user_input[2]+user_input[3]
                    self.records_count=user_input[4]
                    self.temp_arr=np.zeros((int(self.records_count),0),int)
                    
        except FileNotFoundError:
            print("Specified input configuration file doesn't exist. Please check the file. ")
            print("exiting..")
            sys.exit(3)
                               
        
            
    def read_dml(self,dml_file):
        try:
            with open(dml_file) as metadata:
                lines=metadata.readlines()[1:-1]
            return lines
        except FileNotFoundError:
            print("Specified DML file doesn't exist. Please check the file. ")
            print("exiting..")
            sys.exit(4)
    
    def write_output_file(self):
        df=pd.DataFrame(self.temp_arr,columns=self.header)
        print(df)
        df.to_csv(self.output_file,index=False)
        
if __name__=='__main__':
    cls_obj=TestDataGenerator()
    dg=dataGenerator()
    cls_obj.argv_check(sys.argv)
    cls_obj.input_config_file_validation(sys.argv[1])
    dml=cls_obj.read_dml(cls_obj.dml_file_name)
        
    for field in dml:
            cls_obj.columns_name=re.sub('[();]',' ',field.lstrip()).split()
            if cls_obj.columns_name[0]=='decimal':
                cls_obj.test_data=dg.random_decimal_gen(cls_obj.columns_name,int(cls_obj.records_count))
                
            elif cls_obj.columns_name[0]=='string':
                if (re.search('_name',cls_obj.columns_name[2].lower()) or re.search('_nm',cls_obj.columns_name[2].lower())):
                    cls_obj.test_data=dg.random_name_gen(int(cls_obj.records_count))
                    
                elif (re.search('address',cls_obj.columns_name[2].lower()) or re.search('add',cls_obj.columns_name[2].lower())):
                    cls_obj.test_data=dg.random_address_gen(int(cls_obj.records_count))
                    
                else:   
                    cls_obj.test_data=dg.random_string_gen(cls_obj.columns_name,int(cls_obj.records_count))
                    
            elif cls_obj.columns_name[0]=='date':
                cls_obj.test_data=dg.random_date_gen(int(cls_obj.records_count))
                
            cls_obj.header.append(cls_obj.columns_name[2])
            cls_obj.temp_arr=np.column_stack((cls_obj.temp_arr,cls_obj.test_data))
                                
    cls_obj.write_output_file()
    