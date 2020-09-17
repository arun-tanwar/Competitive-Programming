def wave(people):
    lst=[]
    for i in range(len(people[:])):
        if ord(people[i])>=97 and ord(people[i])<=122:
            up=people[i].upper()
            c=people[:i]+up+people[i+1:]
            lst.append(c)
    return lst
