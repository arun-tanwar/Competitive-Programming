def find_uniq(arr):
    n=0
    seq=list(set(arr))
    for i in seq:
        if arr.count(i)==1:
            n=i
            break
    return n
            
