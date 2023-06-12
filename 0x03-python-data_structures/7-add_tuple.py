def add_tuple(tuple_a=(), tuple_b=()):
    num1_a = tuple_a[0] if len(tuple_a) > 0 else 0
    num2_a = tuple_a[1] if len(tuple_a) > 1 else 0
    num1_b = tuple_b[0] if len(tuple_b) > 0 else 0
    num2_b = tuple_b[1] if len(tuple_b) > 1 else 0
    tuple_sum = num1_a + num1_b, num2_a + num2_b
    return tuple_sum
