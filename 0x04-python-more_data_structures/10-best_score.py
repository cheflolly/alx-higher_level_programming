#!/usr/bin/python3
def best_score(a_dictionary):
    for x in a_dictionary:
        if x not in a_dictionary:
            return (None)
    h = sorted(a_dictionary.get(x))
    return (h)
