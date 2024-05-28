def camel_case(s):
    res = s.split(" ")
    ret = ""
    for i in res:
        ret += i.capitalize()
    return ret

print(camel_case("hello case"))