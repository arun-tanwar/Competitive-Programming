l=int(input())
n=int(input())
for i in range(n):
    v1=list(map(int,input().split()))
    w=v1[0]
    h=v1[1]
    if(w<l):
        print('UPLOAD ANOTHER')
    elif(h<l):
        print('UPLOAD ANOTHER')
    elif(w==h):
        print("ACCEPTED")
    else:
        print("CROP IT")
