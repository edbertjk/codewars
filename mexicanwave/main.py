def wave(people):
    index = 0
    array = []
    for i in range(len(people)):
        if people[index] != " ":
            array.append(people[:index] + people[index].capitalize() + people[index + 1:])
        index += 1
    return array

print(wave("two skwdwdw dawd"))