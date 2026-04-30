class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        def co(a):
            count=0
            while a>0:
                if a&1==1:
                    count+=1
                a=a>>1
            return count
        
        for i in range(n+1):
            res.append(co(i))
        return res

        