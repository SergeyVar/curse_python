# Обход по индексам
# lst_1=[[1,2,3],[2,3,4] ,[3,4,5],[4,5,6] ]
# for i in range(len(lst_1)):
#     for j in range(len(lst_1[i])):
#         print(lst_1[i][j],end=' ')
#     print()

# Создание матрицы с 0
# n=int(input())
# m=int(input())
# lst_1=[0]*n
# for i in range(n):
#     lst_1[i]=[0]*m
# for i in range(len(lst_1)):
#     for j in range(len(lst_1[i])):
#         print(lst_1[i][j],end='  ')
#     print()

#
# n = int(input())
# m = int(input())
# lst_1 = []
# for i in range(n):
#     a = [0] * m
#     lst_1.append(a)
# for i in range(len(lst_1)):
#     for j in range(len(lst_1[i])):
#         print(lst_1[i][j],end='  ')
#     print()
# Ввод списка
# lst_1=[]
# n=int(input())
# for i in range(n):
#     x=input().split()
#     for i in range(len(x)):
#         x[i]=int(x[i])
#     lst_1.append(x)
# print(lst_1)


# def modify_list(l):
#     k=0
#     len_l=len(l)
#     for i in l:
#         if i % 2 == 0:
#             a = i // 2
#             l.append(a)
#         k +=1
#         if k==len_l:
#             break
#     del l[0:len_l]

#cool
# def modify_list(l):
#     l[:] = [i//2 for i in l if i % 2 == 0]
# l=[1,2,3,4]
# modify_list(l)
# print(l)

with open('C:/1/dataset_3363_2.txt','r') as a:
    for s in a:
        s=s.strip()

l=[]
l1=[]
l2=[]
for i in range(len(s)-1):
    if s[i].isalpha()==True and s[i+1].isdigit()==True and s[(i+2)-len(s)].isalpha()==True :
        a=int(s[i+1])
        l.append(a)
    if s[i].isdigit()== True and s[i+1].isdigit()==True:
        a=(int(s[i]+s[i+1]))
        l.append(a)
    if  s[i].isalpha()==True:
        l1.append(s[i])
print(l)
print(l1)
for i in range(0,len(l1)):
    l2.append(l1[i]*l[i])
l2=''.join(l2)

with open('C:/1/dataset_3363_2.txt','w') as a:
     a.write(l2)














