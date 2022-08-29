#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for E in range(0, len(matrix)):
            for F in range(0, len(matrix[E])):
                if F != len(matrix[E]) - 1:
                    print(matrix[E][F], end=" ")
                else:
                    print(matrix[E][F])
