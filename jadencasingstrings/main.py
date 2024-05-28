def to_jaden_case(string):
    string = string.split(" ")
    res = [i.capitalize() for i in string]
    return " ".join(res)

print(to_jaden_case("hello World"))
