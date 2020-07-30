from itertools import permutations
 
#t = int(input())
t = 1
 
while t > 0:
    #print(t)
    #n = int(input())
    arr = [int(x) for x in input().split()]
 
    ok = False
    for l in [list(x) for x in list(permutations(arr, 6))]:
        if sum(l[:3]) == sum(l[3:]):
            print("YES")
            ok = True
            break
    if not ok:
        print("NO")
        #print(f'{l[:3]} - {l[3:]}')
 
    t -= 1