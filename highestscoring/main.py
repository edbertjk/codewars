def high(x):
    result = x.split(" ")
    i = 0
    strres = ""
    res = 0
    dict = {}
    current_letter = 'a'
    while current_letter <= 'z':
        i += 1
        dict[current_letter] = i
        current_letter = chr(ord(current_letter) + 1)

    for i in result:
        wrapRes = 0
        for e in range(len(i)):
            wrapRes += dict[i[e]]
        if res < wrapRes:
            strres = i
            res = wrapRes
    return strres

print(high("ss yy"))
