tc=int(input())
for i in range(tc):
    bag,k_time=map(int,input().split(' '))
    candies_bag=[int(j) for j in input().strip().split()[:bag]]
    res=0
    for _ in range(k_time):
        vlu_taken=max(candies_bag)
        res+=vlu_taken
        nw_vlu=vlu_taken//2
        n=candies_bag.index(vlu_taken)
        candies_bag[n]=nw_vlu
    print(res)
