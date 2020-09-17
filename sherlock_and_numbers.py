tc=int(input())
for i in range(tc):
    n,k,p=map(int,input().split(" "))
    lst=[]
    lst2=[int(_) for _ in input().strip().split()][:k]
    for j in range(1,n+1):
        lst.append(j)
    for L in lst2:
        lst.remove(L)
    if len(lst)>=p:
        print(lst[p-1])
    else:
        print("-1")
