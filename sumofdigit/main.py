def digital_root(n):
    return n if n <= 9 else digital_root(sum(int(i) for i in str(n)))

print(digital_root(199))