n = int(input())
result = "NO"
for i in range(n):
    line = input()
    data = line.split()
    before = int(data[1])
    after = int(data[2])
    if before >= 2400 and after > before:
        result = "YES"
        break
 
print(result)
