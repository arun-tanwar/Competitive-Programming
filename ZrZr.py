tc=int(input())
def findTrailingZeros(n):
    count=0
    while n:
        count+=n//5
        n//=5
    print(count)

for _ in range(tc):
    n=int(input())
    findTrailingZeros(n)
