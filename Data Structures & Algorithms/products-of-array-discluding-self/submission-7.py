class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n

        l=1
        for i in range(n):
            res[i]=l
            l*=nums[i]

        r=1
        for j in range(n-1,-1,-1):
            res[j]*=r
            r*=nums[j]

        return res

