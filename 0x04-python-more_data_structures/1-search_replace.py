#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        new_list.append(i)
    new_list[new_list.index(search)] = replace
    return new_list
