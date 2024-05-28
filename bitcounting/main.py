def count_bits(n):
    binary = bin(n)
    return binary.count("1")

print(count_bits(10))