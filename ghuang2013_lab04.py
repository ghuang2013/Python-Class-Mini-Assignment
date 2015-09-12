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


def read_file(filename):
    try:
        file_in = open(filename)
    except FileNotFoundError as e:
        print("Error: ", e.strerror)
        raise FileNotFoundError
    return file_in


def make_dict():
    try:
        city_records = dict()
        file_in = read_file("fl_cities.txt")
        for line in file_in:
            zipcode, city = line.rstrip().split(':')
            city_records[city] = zipcode
    except FileNotFoundError:
        print("The system is unable to locate the record file")
        exit()
    else:
        file_in.close()
    return city_records


def test_dict(record):
    try:
        file_in = read_file("fl_maint.txt")
        for line in file_in:
            process_command(line, record)
    except FileNotFoundError:
        print("The system is unable to locate test cases")
        exit()
    else:
        file_in.close()


def print_dict(dict_record):
    for key, value in sorted(dict_record.items()):
        print_tuple((key, value), 15)


def update(dict_record, key, new_val):
    if key not in dict_record:
        return "city unknown"
    dict_record[key] = new_val
    return new_val


def print_tuple(tup, width):
    print("{:{width}s} {:{width}s}".format(*tup, width=width))


def process_command(line, record):
    errstr = "city unknown"
    line = line.rstrip()
    print('\n>>', line)
    try:
        unity, args = line.split('-')
        if unity == Command.Print_Sorted_Cities.value and args == "cities":
            print_dict(record)
        elif unity == Command.Find_Zip_Code.value:
            print_tuple((args, record.get(args, errstr)), 15)
        elif unity == Command.Change_Zip_Code.value:
            new_zipcode, city_name = args.split(':')
            print_tuple((city_name, update(record, city_name, new_zipcode)), 15)
        else:
            print("unknown cmd")
    except ValueError as e:
        print("Argument Error:", e.__str__())


def main():
    city_records = make_dict()
    test_dict(city_records)


if __name__ == "__main__":
    main()
