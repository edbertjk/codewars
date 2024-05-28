def multiplication_table(size):
    if size == 1:
        return [1]
    sum = size * size
    index = 0
    array1 = []
    array2 = []
    while index != sum:
        for i in range(size):
            index += i
            array1.append(index)
        array2.append(array1)
        print(array2)

multiplication_table(3)