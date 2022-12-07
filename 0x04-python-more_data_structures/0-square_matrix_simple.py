#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    for x in matrix:
        new_matrix.append([])
        for y in matrix[i]:
            new_matrix[i].append(y**2)
        i += 1
    return (new_matrix)
