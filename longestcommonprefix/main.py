def fun(strs):
    word = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return word

        word += strs[0][i]
    return word