def count_smileys(arr):
    smiley = 0
    for i in arr:
        if((i[0]==':' or i[0]==';')):
            if((i[1]=='-' or i[1]=='~')):
                if ((i[2]==')' or i[2]=='D')):
                    smiley+=1
            elif ((i[1]==')' or i[1]=='D')):
                smiley+=1   
    return smiley
                    
                
