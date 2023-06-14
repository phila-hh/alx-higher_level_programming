#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_sum = 0
    length = 0
    for x, y in my_list:
        total_sum += x * y
        length += y
    average = total_sum / length
    return average
