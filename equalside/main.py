def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[1+i:]) == sum(arr[:i]):
            return i
    return -1

print(find_even_index([1,2,3,4,3,2,1]))