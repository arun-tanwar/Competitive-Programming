tc=int(input())
for m in range(tc):
    inp=list(map(int,input()))
    inp=sorted(inp)
    k=inp[-1]
    j=len(inp)
    count=0
    i=0
    while(inp[i]!=k):
        l=inp[i]
        l+=1
        if l==inp[i+1]:
            count+=1
        i+=1
    count+=1
    if count==j:
        print("YES")
    else:
        print("NO")
