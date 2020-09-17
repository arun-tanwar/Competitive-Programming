tc=int(input())
lst= [int(i) for i in input().split(' ')][:tc]
def mul(lst):
    x=1
    for j in lst:
        x=(x*j)%(10**9+7)
    print(x)
mul(lst)
