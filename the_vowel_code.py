def encode(st):
    strob=''
    for i in st:
        if i=='a':
            strob +='1'
        elif i=='e':
            strob +='2'
        elif i=='i':
            strob +='3'
        elif i=='o':
            strob +='4'
        elif i=='u':
            strob +='5'
        else:
            strob+=i
    return strob
    
def decode(st):
    strob=''
    for i in st:
        if i=='1':
            strob +='a'
        elif i=='2':
            strob +='e'
        elif i=='3':
            strob +='i'
        elif i=='4':
            strob +='o'
        elif i=='5':
            strob +='u'
        else:
            strob+=i
    return strob
