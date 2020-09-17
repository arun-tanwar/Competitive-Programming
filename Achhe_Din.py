tc=int(input())
n=0
for i in range(tc):
    k=int(input())
    lst =[int(x) for x in input().strip().split()[:k]]
    new_lst=list(set(lst))
    for j in new_lst:
        if lst.count(j)==1:
            print(j)
            break    

