n = int(input())
arr = [int(x) for x in input().split()]
 
arr2 = []
maxL = -1
if len(arr)==1:
    print(1)
else:
    for i in range(n-1):
        if i==0:
            arr2.append(i)
        if arr[i+1]>=arr[i]:
            arr2.append(arr[i])
        else:
            maxL = max(maxL, len(arr2))
            arr2 = []
            arr2.append(arr[i])
 
    print(max(maxL, len(arr2)))