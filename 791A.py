i = input().split()
a = int(i[0])
b = int(i[1])
 
i = 0
while a <= b:
    a*=3
    b*=2
    i+=1
 
print(i)
