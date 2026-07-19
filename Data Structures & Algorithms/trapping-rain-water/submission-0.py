class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n=len(height)
        res=0

        for i in range(n):
            lmax=rmax=height[i]

            for j in range(i):
                lmax=max(lmax,height[j])

            for k in range(i+1,n):
                rmax=max(rmax,height[k])

            res+=min(lmax,rmax)-height[i]

        return res
        