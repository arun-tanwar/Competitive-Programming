    stri = str(input(""))
     
    num=0
    num2=0
    cnt=0
    cnt1=0
    seq = list(set(stri))
    seq = ''.join(sorted(seq))
    num = seq[0]
    num2 = seq[1]
    stri = ''.join(sorted(stri))
     
    cnt=stri.count(num2)
    cnt1=stri.count(num)
    cnt=cnt*2
    if cnt==cnt1:
        print("Yes")
    else:
        print("No")
