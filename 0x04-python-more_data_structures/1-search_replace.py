#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = 0
    for x in my_list:
        if x is search:
            Newlist[i] = replace
        i += 1
    return (new_list)
