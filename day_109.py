# Given an unsigned 8-bit integer, swap its even and odd bits. 
# The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
def swap(value):
    return (value & 0b10101010) >> 1 | (value & 0b01010101)

