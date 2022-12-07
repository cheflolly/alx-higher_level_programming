#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary:
        new_value = (a_dictionary.get(i)) * 2
        new_dict.update({i: new_value})
    return (new_dict)
