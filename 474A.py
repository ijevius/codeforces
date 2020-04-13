st = "qwertyuiop"
nd = "asdfghjkl;"
d = "zxcvbnm,./"

letter = input()
text = input()
result = list()

for i in range(len(text)):
    if text[i] in st:
        if letter == 'R': result.append(st[st.find(text[i])-1])
        else: result.append(st[st.find(text[i])+1])
    elif text[i] in nd:
        if letter == 'R':
            result.append(nd[nd.find(text[i]) - 1])
        else:
            result.append(nd[nd.find(text[i]) + 1])
    else:
        if letter == 'R':
            result.append(d[d.find(text[i]) - 1])
        else:
            result.append(d[d.find(text[i]) + 1])


print("".join(result))
