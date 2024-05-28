def move_zeros(lst):
    for e in range(len(lst)):
        if lst[e] < 1 and e+1 != len(lst):
            lst[e], lst[e+1] = lst[e+1], lst[e]
            print(e)
    return lst

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))