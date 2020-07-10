import testdata as td
from faker import Faker

fake = Faker()

"""
This module generates test data with respect to the data type
data types supported:
    1. decimal
    2. string
    3. date
"""


class TestDataEngine:
    def __init__(self):
        self.values = []

    # Generates decimal data
    def get_decimal_test_data(self, column, record_count):
        self.values.clear()
        if '.' in column[1]:
            digit_len = int(column[1].split('.')[0])
            for _ in range(record_count):
                self.values.append(int(td.get_digits(digit_len)) / 100)
        else:
            for _ in range(record_count):
                self.values.append(int(td.get_digits(int(column[1]))))
        return self.values

    # Generates string_data
    def get_string_test_data(self, column, record_count):
        self.values.clear()
        for _ in range(record_count):
            self.values.append(td.get_ascii_string(int(column[1])))
        return self.values

    # Generates date data
    def get_date_test_data(self, column, record_count):
        self.values.clear()
        for _ in range(record_count):
            self.values.append(fake.date("%Y%m%d"))
        return self.values
