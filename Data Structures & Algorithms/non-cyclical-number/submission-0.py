class Solution:
    def isHappy(self, n: int) -> bool:
        def sp(m):
            t=0
            while m>0:
                d=m%10
                t+=d*d
                m//=10
            return t

        visit=set()
        while n!=1:
            if n in visit:
                return False
            
            visit.add(n)
            n=sp(n)
        return True

        

        