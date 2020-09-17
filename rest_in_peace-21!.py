tc=int(input())
for i in range(tc):
    k=int(input())
    
    if (k%21 == 0) or ('21' in str(k)):
        print("The streak is broken!")
    elif k%21 != 0:
        print("The streak lives still in our heart!")
    else:
        pass
