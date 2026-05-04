import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=min(piles)
        r=max(piles)

        while l<=r:
            mid=(l+r)//2
            a=0
            for j in piles:
                a+=math.ceil(j/mid)
            if a>h:
                l=mid+1
            elif a<=h:
                r=mid-1

        return l




        