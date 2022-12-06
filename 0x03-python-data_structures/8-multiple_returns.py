#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return ((len(sentence), None))
    return ((len(sentence), sentence[0]))

# double () because its returning a tuple
