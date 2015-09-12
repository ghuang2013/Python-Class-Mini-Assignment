# Course: COP 4930  - Python Programming
# Term:   Fall 2015 - Dr. Clovis Tondo
# Author: Guan Huang
# Assignment #4
# Due: September 16th, 2015

from enum import Enum


class Command(Enum):
    Print_Sorted_Cities = 'p'
    Find_Zip_Code = 'f'
    Change_Zip_Code = 'c'


class CityDict(dict):
    def __init__(self, *args, **kwargs):
        super(CityDict, self).__init__(self, *args, **kwargs)

    def reverse_key_value(self):
        reversed_dict = dict()
        for key, value in self.items():
            reversed_dict[value] = key
        return reversed_dict

    def print_reversed_sorted(self):
        city_record_reversed = self.reverse_key_value()
        for key in sorted(city_record_reversed):
            print("{:15s} {:10s}".format(key, city_record_reversed[key]))

    def get_key(self, niddle, errstr):
        for kay, value in self.items():
            if value == niddle:
                return kay
        return errstr

    def change_key(self, niddle, newvalue, errstr):
        for kay, value in self.items():
            if value == niddle:
                self[newvalue] = self.pop(kay)
                return newvalue
        return errstr


def read_file(filename):
    try:
        file_in = open(filename)
    except FileNotFoundError as e:
        print("Error: ", e.strerror)
        raise FileNotFoundError
    return file_in


def make_dict():
    try:
        city_records = CityDict()
        file_in = read_file("fl_cities.txt")
        for line in file_in:
            key, value = line.rstrip().split(':')
            city_records[key] = value
    except FileNotFoundError:
        print("The system is unable to locate the record file")
        exit()
    return city_records


def test_dict(record):
    try:
        file_in = read_file("fl_maint.txt")
        for line in file_in:
            process_command(line, record)
    except FileNotFoundError:
        print("The system is unable to locate test cases")
        exit()


def process_command(line, record):
    errstr = "city unknown"
    line = line.rstrip()
    print('\n>>', line)
    try:
        unity, args = line.split('-')
        if unity == Command.Print_Sorted_Cities.value and args == "cities":
            record.print_reversed_sorted()
        elif unity == Command.Find_Zip_Code.value:
            print("{:15s} {:10s}".format(args, record.get_key(args, errstr)))
        elif unity == Command.Change_Zip_Code.value:
            new_zipcode, city_name = args.split(':')
            print("{:15s} {:10s}".format(city_name, record.change_key(city_name, new_zipcode, errstr)))
        else:
            print("unknown cmd")
    except ValueError as e:
        print("Argument Error:", e.__str__())


def main():
    city_records = make_dict()
    test_dict(city_records)


if __name__ == "__main__":
    main()
