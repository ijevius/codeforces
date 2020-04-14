T = int(input())

for t in range(T):
    n = int(input())
    a_s = sorted([int(a) for a in input().split()])
    if n == 2: print(int(a_s[0])^int(a_s[1])); continue
    t_min = int(a_s[0])^int(a_s[1])
    for i in range(1, len(a_s)-1):
        t_min = min(t_min, int(a_s[i])^int(a_s[i+1]))
    print(t_min)
