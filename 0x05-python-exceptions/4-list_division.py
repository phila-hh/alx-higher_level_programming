#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    count = 0
    while count <= list_length - 1:
        d = 0
        try:
            d = my_list_1[count] / my_list_2[count]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(d)
            count += 1
    return result_list
