wins = []
w_d = input().split()
n = int(w_d[0])
d = int(w_d[1])
 
current_wins = 0
for line in range(d):
    s = input()
    if '0' in s:
        wins.append("w")
    else:
        wins.append("l")
 
print(len(max("".join(wins).split("l"), key=len)))
