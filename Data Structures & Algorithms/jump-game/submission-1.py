class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)-1
        for i in range(len(nums)-1):
            i+=nums[i]
            if i==l:
                return True
        return False
        