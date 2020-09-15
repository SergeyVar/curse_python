a1=[]
a= open('C:/1/dataset_3363_3.txt','r')
s=a.read().strip().lower()
a=list(s.split(' '))
a.sort()
for i in range(len(a)):
    a1.append(a.count(a[i]))
dic1 = dict(zip(a, a1))
d=max(dic1, key=dic1.get)
print(s)
print(a)
print(a1)
print(dic1)
print(d,dic1.setdefault(d))