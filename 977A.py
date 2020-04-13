def mo(num):
    if not str(num).endswith("0"):
        return num-1
    else:
        return int(num/10)
 
 
a = input().split()
n = int(a[0])
k = int(a[1])
res = n
for i in range(k):
    res = mo(res)
 
print(res)
