def alphabet_position(text):
    index = 0
    first_char = 'a'
    dict = {}
    while first_char <= 'z':
        index += 1
        dict[first_char] = index
        first_char = chr(ord(first_char) + 1)
    for i in text:

