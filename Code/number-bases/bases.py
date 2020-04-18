#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

hexi = []
for letter in string.hexdigits:
    if letter.lower() in hexi:
        pass
    else:
        hexi.append(letter)


def bin_to_base10(number):
    number = int(number)
    power = 0
    decimal = 0
    while number > 0:
        decimal += 2 ** power * (number % 10)
        number //= 10
        power += 1
    return decimal


def get_digit(number):

    for x in range(len(hexi)):
        if number == hexi[x]:
            print(x)
            return x


def hex_to_base10(number):

    decimal = 0
    power = 0
    for digit in range(len(number), 0, -1):
        decimal = decimal + 16 ** power * get_digit(number[digit-1])
        power += 1
    return decimal


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # TODO: Decode digits from binary (base 2)
    # ...

    if base == 2:
        return bin_to_base10(digits)

    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    if base == 16:
        return hex_to_base10(digits)
        # makes list of hexidecimal values


def base10_to_binary(number):
    binary = 0
    power = 0
    while number > 0:
        binary += 10 ** power * (number % 2)
        number //= 2
        power += 1
    return binary


def base10_to_hex(number):
    hexi = 0
    power = 0
    hex_mod = number % 4
    while number > 0:
        if hex_mod != 0:
            dif = 4 - hex_mod
        for i in dif:


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    if base == 2:
        return base10_to_binary(number)
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    if base == 16:
        return base10_to_hex(number)
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    if base1 == 2 and base2 == 16:
        base = bin_to_base10(digits)
        base10_to_hex(base)
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


def test():
    print(decode('10101', 2))
    print(decode('10101', 16))
    print(encode(21, 2))
    print(encode(10101, 16))


if __name__ == '__main__':
    # main()
    test()
