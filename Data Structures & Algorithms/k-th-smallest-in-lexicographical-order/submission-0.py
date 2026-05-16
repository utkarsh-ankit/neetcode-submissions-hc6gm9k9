class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur=1
        i=1

        def count(cur):
            res=0
            
            neigh=cur+1
            while cur<=n:
                res+=min(neigh,n+1)-cur
                cur*=10
                neigh*=10
            return res

        while i<k:
            steps=count(cur)
            if i+steps<=k:
                cur=cur+1
                i+=steps
            else:
                cur*=10
                i+=1
        return cur
        