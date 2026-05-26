class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax=gmin=nums[0]
        cmax=cmin=0
        total=0
        for i in nums:
            cmax=max(cmax+i,i)
            cmin=min(cmin+ i, i)
            total+= i
            gmax=max(gmax,cmax)
            gmin=min(gmin,cmin)
        return max(gmax,total-gmin) if gmax>0 else gmax
        