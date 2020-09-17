tc=int(input())
lst=[]
for i in range(tc):
    ele=int(input())
    lst.append(ele)
for j in lst:
    def func(n):
        ad=1+((n*(n+1))//2)
        print(ad)
    func(j)
