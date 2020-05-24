t = int(input())
 
for x in range(t):
    n = int(input())
    s = [int(i) for i in input().split()]
    s = sorted(s, reverse=True)
    #print(s)
    m = s[0]
    for i in range(1, len(s)):
        #print(s[:i], ":", s[i:])
        #print(f"min left = {s[:i][-1]} max right = {s[i:][0]}")
        m = min(m, int(s[:i][-1])-int(s[i:][0]))
    print(m)
