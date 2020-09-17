N=int(input())
n=[int(i) for i in input().strip().split() [:N]]
k=[]
count=0
if n!=[]:
        count+=1
for i in range(len(n)-1):
    if n[i+1]<n[i]:
        count+=1
print(count)
