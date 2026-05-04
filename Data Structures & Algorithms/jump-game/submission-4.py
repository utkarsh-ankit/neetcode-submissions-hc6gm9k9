class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)-1
        if l==0:
            return True
        for i in range(len(nums)):
            i+=nums[i]
            if i==l:
                return True
        return False