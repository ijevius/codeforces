def isP(num):
    if (num <= 1):
        return False
    if (num <= 3):
        return True
    if (num % 2 == 0 or num % 3 == 0):
        return False
    i = 5
    while (i * i <= num):
        if (num % i == 0 or num % (i + 2) == 0):
            return False
        i = i + 6
 
    return True
 
n = int(input())
 
for b in range(4, 999999999):
    if not isP(b):
        if not isP(n+b):
            print(f"{n+b} {b}")
            break
