def reverse_int_w_stack(number):
    number = str(number)
    new_number = []
    for i in number[::-1]:
        new_number.append(i)
    return ''.join(new_number)


print(reverse_int_w_stack(3749))
