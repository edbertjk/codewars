def dig_pow(n, p):
    returnV = 0;
    res = 0;
    for i in range(len(str(n))):
        res += int(str(n)[i]) ** p
        p += 1

    print()
    returnV += int(res / n)
    if (returnV > 0 and isinstance(returnV, int)): return returnV
    return -1

print(dig_pow(46288, 10))