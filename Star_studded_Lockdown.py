for i in range(int(input())):
    tc=int(input())
    s=input()
    count=0
    for c in set(s):
        x=s.count(c)
        count += x*(x-1)//2
    print(count)
