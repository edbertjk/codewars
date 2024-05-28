import re
def to_camel_case(text):
    wrapper = re.split("[_-]", text)
    res = ""
    index = 0
    for i in wrapper:
        if index == 0:
            res += i.lower()
        else:
            res += i.capitalize()
        index += 1
    return res

print(to_camel_case(""))