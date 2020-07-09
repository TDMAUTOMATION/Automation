# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json


s_dict={"metadata" :["firstname","lastname","email","phone"],
        "no_of_records": 10,
        "output_file_format": ".txt"
        }

source_file="C:/Users/home/TestDataGenerator/input.json"

f=open(source_file,'w')
f.write(json.dumps(s_dict))
f.close()

