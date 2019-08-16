def count_set_bits(bits):
    # Brian Kernighan's algorithm
    count = 0
    while bits > 0:
        # bits - 1 flips all bits up to first set bit
        # doesn't touch anything on the left side of set bit
        # will be done as many times as there are set bits
        # as one bit is unset at each loop step
        bits = bits & (bits - 1)
        count += 1
    return count


def count_set_bitscheck(bits):
    return sum([1 for idx in str(bin(bits)) if idx == "1"])


if __name__ == "__main__":
    all_bits = [0, 1, 100, 10002, 217647389]
    for bits in all_bits:
        assert count_set_bits(bits) == count_set_bitscheck(bits), '{} != {}'.format(count_set_bits(10002), count_set_bitscheck(bit))
