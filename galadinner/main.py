input1 = str(input("")).split(" ")
wrap = 0
for i in range(int(input1[0])):
    input2 = str(input("")).split(" ")
    wrap += int(input2[0]) * int(input2[1])
if int(input1[1]) <= wrap:
    print("YES")
else:
    print("NO")
