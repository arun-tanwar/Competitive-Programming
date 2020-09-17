tc=int(input())
for k in range(tc):
    n,a,b,c=map(int,input().split())
    lst=[]
    count=0
    for i in range(1,n+1):
        lst.append(i)
    for j in lst:
        if((j%a==0)or(j%b==0)or(j%c==0)):
            count+=1
    print(count)
