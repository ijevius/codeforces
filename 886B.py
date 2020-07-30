n = int(input())
myd = {}
arr = [int(x) for x in input().split()]
 
for i in range(n):
    myd[arr[i]] = i
 
print(arr[min(myd.values())])