#!/usr/bin/python3
""" A module include a function to validate UTF8 """


def validUTF8(data):
    """ UTF8 validation """
    number_of_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            while mask & num:
                number_of_bytes += 1
                mask = mask >> 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
