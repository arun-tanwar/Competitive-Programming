tc=int(input())
arr=[]
op_ele=0
res=0
for i in range(tc):
    n,k=map(int,input().split())
    arr=[int(j) for j in input().strip().split() [:n]]
    op_ele=min(arr)
    if op_ele>=k:
        print("0")
    else:
        print(k-op_ele)
    
