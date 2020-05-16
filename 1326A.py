nums = int(input())
 
 
def p(n):
    min = int('2' + '2' * (n - 1))
    max = int('9' * n)
 
    for k in range(max, min - 1, -1):
        dividers = set(str(k))
        ok = False
        if not '0' in str(k) and not '1' in str(k):
            for div in dividers:
                if k % int(div) == 0:
                    ok = False
                    break
                else:
                    ok = True
            if ok:
                print(k)
                return
 
    print(-1)
 
 
for m in range(nums):
    p(int(input()))
