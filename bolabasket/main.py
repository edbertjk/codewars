N,D = [int(x) for x in input().split(" ")]
PI = [int(x) for x in input().split(" ")]
res = 0;
winning = 0;

for n in PI:
    res += n
    
while D < res:
    res -= D
    winning += 1

print(winning)
