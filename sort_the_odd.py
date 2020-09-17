def sort_array(source_array):
    odd=sorted([n for n in source_array if n%2!=0])
    c=0
    lst=[]
    for i in source_array:
        if i%2!=0:
            lst.append(odd[c])
            c+=1
        else:
            lst.append(i)
    return lst
    
