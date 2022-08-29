#!/usr/bin/python3


def no_c(my_string):
    new_str = [E for E in my_string if E != "c" if E != "C"]
    return "".join(new_str)
