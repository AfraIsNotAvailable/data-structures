"""
    Fundamental bit operations
    get_bit: get the bit at the ith position
    set_bit: set bit at the ith position
    clear_bit: clear bit at ith position
    update_bit: update bit at ith position
"""

def get_bit(num: int, i: int) -> int:
    return int((num & (1 << i)) != 0)