def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    x = my_list[0]
    for n in my_list:
        if n > x:
            x = n

    return x
