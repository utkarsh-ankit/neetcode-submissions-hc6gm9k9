class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)-1
        for i in range(len(nums)):
            i+=nums[i]
            if i==l:
                return True
        return False
        