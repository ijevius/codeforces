t = int(input())

for i in range(t):
    #result = 0
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    if a%b==0:
        print(0)
        continue
    elif a<b:
        print(b-a)
        continue
    elif a==b:
        print(0)
        continue
    else:
        k = a
        #while not np.mod(k,b)==0:
        #    print(f"k={k} b={b} mod = {np.mod(k,b)}")
        #    k+=1
        #    result+=1
        x = 2*b-a
        if x>0: print(x)
        else: print(f"{b-(a%b)}")
        #print(result)
