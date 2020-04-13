tests = int(input())
for i in range(tests):
    chunk = 0
    line = input().split()
    s = int(line[0]) 
    a = int(line[1]) 
    b = int(line[2]) 
    c = int(line[3]) 
    if s<c:
        print(0)
        continue
    else:
        to_buy = s//c 
        chunk += to_buy
        if to_buy >= a:
            chunk += (to_buy//a)*b
        print(chunk)
