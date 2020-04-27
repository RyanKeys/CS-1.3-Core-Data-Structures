#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def get_base(base):
    count = "0"
    chars = string.digits + string.ascii_lowercase

    for i in range(base-1):
        count += chars[i+1]
    return count


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # TODO: Decode digits from binary (base 2)
    # ...

    decode = 0
    base_range = get_base(base)
    power = 0
    for digit in digits[::-1]:
        for i in range(len(base_range)):
            if digit == base_range[i]:
                decode += (base**power) * i
        power += 1
    return decode


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    curr_base = get_base(base)
    sol = ""
    while True:
        remainder = number % base
        number = number // base
        sol += curr_base[remainder]
        if number == 0:
            return sol[::1]


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
    if base1 == 10:
        sol = encode(int(digits), base2)
    elif base2 == 10:
        sol = decode(digits, base1)
    else:
        base10 = decode(digits, base1)
        sol = encode(int(base10), base2)
    return sol


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
    print(convert("10101", 16, 10))
    print(convert("10101", 2, 10))


if __name__ == '__main__':
    main()
    test()
