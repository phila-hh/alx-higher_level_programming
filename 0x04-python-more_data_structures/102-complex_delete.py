#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    value_list = list(a_dictionary.values())
    key_list = list(a_dictionary.keys())
    if value not in value_list:
        return a_dictionary

    for key in key_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
