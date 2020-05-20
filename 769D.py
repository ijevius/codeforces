def interesting(x, z):
    return int(str(int(bin(x)[2:])^int(bin(z)[2:])).count("1"))

n, K = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
result = 0
#print(interesting(5, 3))
for i in range(len(a)-1):
    for k in range(i+1, len(a)):
        if interesting(a[i], a[k])==K:
            result+=1
            #print(f"пара {a[i]} {a[k]} интересная")

#print(f"result is {result}")
print(result)
