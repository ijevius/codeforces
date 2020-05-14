t = int(input())
for T in range(t):
    n, k = [int(num) for num in input().split()]
    a = sorted([int(aS) for aS in input().split()], reverse=False)
    b = sorted([int(bS) for bS in input().split()], reverse=True)

    for i in range(k):
        a[0], b[0] = max(b[0], a[0]), min(b[0], a[0])
        a = sorted(a, reverse=False)
        b = sorted(b, reverse=True)

    print(sum(a))
