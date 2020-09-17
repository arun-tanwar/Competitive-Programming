class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lst=[]
        cnt=0
        cnt1=0
        sml=0
        lst2=[]
        cnt=S.count("I")
        cnt1=S.count("D")
        k=cnt1+cnt
        lrg=k
        for i in range(0,k+1):
            lst.append(i)
        for _ in S:
            if _=="I":
                lst2.append(sml)
                sml+=1
            elif _=="D":
                lst2.append(lrg)
                lrg-=1
            if sml == lrg:
                lst2.append(sml)
        return lst2
        
            
