#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]
        for E in my_list:
            if E > max_value:
                max_value = i
        return max_value
    return None
