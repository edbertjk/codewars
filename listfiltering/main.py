def checking(e):
    res = []
    for arr in e:
        if isinstance(arr, int):
            res.append(arr)

    return res

print(checking(["2", "2", 3]))