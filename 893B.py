orig = int(input())
n = orig
while n>0:

    if orig%n==0:        
        bn = bin(n)[2:]
        if bn.split("0")[0] == len(bn.split("0")[0]) * bn.split("0")[0][0]:            
            if (len(bn.split("0")[1:])+1==len(bn.split("0")[0]) and "".join(bn.split("0")[1:])==""):                
                print(n)
                break
    n -= 1