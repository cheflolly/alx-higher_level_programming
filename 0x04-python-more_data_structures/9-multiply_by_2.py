#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    {x: get(x)*2 for x in a_dictionary}
    new_dict.update(a_dictionary)
    return (new_dict)


"""
    for i in a_dictionary:
        new_value = (a_dictionary.get(i)) * 2
        new_dict.update({i: new_value})
    return (new_dict)
    """
