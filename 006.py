s='a3b4c2e10b1'

l=[]
l1=[]
for i in range(len(s)-1):
    if s[i] in 'abcdefghijklmnopqrstuvwxyz' or s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        l.append(s[i])
    elif s[i] in '0123456789' and s[i+1] in'0123456789':
        l1.append((s[i]+s[i+1]))

print(l)
print(l1)
