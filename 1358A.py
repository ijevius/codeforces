t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    s = n*m
    if s==1: print(1); continue
    for s2 in range(s, s+3):
        if s2%2==0:
            print(int(s2/2))
            break