import itertools
n = int(input())


def very_happy(num):
    banned = '01235689'
    for c in banned:
        if c in str(num):
            return False
    if not str(num).count('4') == str(num).count('7'):
        return False
    else:
        return True


if very_happy(n):
    print(n)
else:
    candidats2 = []
    for add in range(3):
        candidats = list(itertools.product(['4', '7'], repeat=len(str(n))+add))
        candidats2.append(sorted([int("".join(list(can))) for can in candidats if very_happy(can)]))
    candidats2 = [item for sublist in candidats2 for item in sublist]
    for x in candidats2:
        if x > n:
            print(x)
            break         
