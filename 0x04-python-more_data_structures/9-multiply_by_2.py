#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    {x*2 for x in a_dictionary}
    new_dict.update(a_dictionary)
    return (new_dict)
