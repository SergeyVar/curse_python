# def f(x):
#     return x+1
# dic_1={}
# lst_1=[]
# n=int(input())
# for x in range(n):
#     x=int(input())
#     if x in dic_1:
#         lst_1.append(dic_1[x])
#     if x not in dic_1:
#         dic_1[x]=f(x)
#         lst_1.append(dic_1[x])
# for i in lst_1:
#     print(i)


#
# with open('C:/1/robots.txt','r') as a:
#     for s in a:
#         s=s.strip()
#         print(s)
# with open('C:/1/robots.txt','w') as a:
#     a.write('a3b4c2e10b1')
a=[]
a1=[]
with open('C:/1/dataset_3363_3.txt','r') as a:
    for s in a:
        s=s.strip().lower()
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











