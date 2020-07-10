import pandas as pd
import numpy as np
import re
from TestDataEngine import TestDataEngine
import sys

"""
Project name: Test data Generation
Author: Jayaprakash. M

This python modules reads the Abinitio dml file and creates an output file with 
test data as per the data types specified in the dml. 
This module currently supports fixed length record format
Parameters required:
    param 1: dml_file_name
    param 2: output_file_name
    param 3: record_count

Todo's: 
    1. Generate test data for variable length record formats. (fields delimited with delimiter)
    2. Given an input file, create test data for the specified columns to replace the NPI/PCI columns.
    3. Adding logs
"""


class TestDataGenerator():
    def __init__(self):
        self.header = []
        self.column = []
        self.dml_file_name = ''
        self.output_file = ''
        self.record_count = 10
        self.temp_ar = []
        self.test_data = []

    def read_dml(self, dml_file):
        try:
            with open(dml_file) as schema:
                # ignore the lines record and end in the dml file
                lines = schema.readlines()[1:-2]
            return lines
        except FileNotFoundError:
            print("DML file is not available. Please check.")
            sys.exit(2)

    def write_output_file(self):
        output_df = pd.DataFrame(self.temp_ar, columns=tdg.header)
        output_df.to_csv(sep=",", path_or_buf=tdg.output_file, header=True, index=False)

    def check_input_arguments(self, argv):
        # read command line arguments
        if len(sys.argv) != 4:
            print("Expected number of arguments not passed.")
            print("Exiting the program.")
            print("Usage: TestDataGenerator.py <dml file> <output file> <no of records")
            sys.exit(2)
        else:
            self.dml_file_name = argv[1]
            self.output_file = argv[2]
            self.record_count = int(argv[3])
            self.temp_ar = np.zeros((self.record_count, 0), int)

    def clear_values(self):
        self.column.clear()
        self.test_data.clear()


if __name__ == '__main__':
    tdg = TestDataGenerator()
    tde = TestDataEngine()
    tdg.check_input_arguments(sys.argv)
    dml = tdg.read_dml(tdg.dml_file_name)
    for line in dml:
        tdg.clear_values()
        tdg.column = re.sub("[();]", ' ', line).split()
        if tdg.column[0] == 'decimal':
            test_data = tde.get_decimal_test_data(tdg.column, tdg.record_count)
        elif tdg.column[0] == 'string':
            test_data = tde.get_string_test_data(tdg.column, tdg.record_count)
        elif tdg.column[0] == 'date':
            test_data = tde.get_date_test_data(tdg.column, tdg.record_count)
        tdg.header.append(tdg.column[2])
        tdg.temp_ar = np.column_stack((tdg.temp_ar, test_data))
    tdg.write_output_file()
