#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        valuE = list(a_dictionary.values())
        keY = list(a_dictionary.keys())
        return (keY[valuE.index(max(valuE))])
