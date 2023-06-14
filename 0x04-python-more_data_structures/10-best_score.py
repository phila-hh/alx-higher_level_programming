#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    keys_list = list(a_dictionary.keys())
    value_list = list(a_dictionary.values())

    max_score = keys_list[value_list.index(max(value_list))]
    return max_score
