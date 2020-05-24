t = int(input())
 
for l in range(t):
    a, b = [int(x) for x in input().split()]
    x2 = min(a, b)*2
    xm = max(a, b)
    diff = abs(xm-x2)
    print((min(x2, xm)+diff)**2)
