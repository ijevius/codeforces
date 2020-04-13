n = input()
if n.endswith('5'):
    n = int(n)+5
elif int(n[len(n)-1]) > 5:
    n = int(n)+(10-int(n[len(n)-1]))
elif int(n[len(n)-1]) < 5:
    n = int(n)-int(n[len(n)-1])
 
print(n)
