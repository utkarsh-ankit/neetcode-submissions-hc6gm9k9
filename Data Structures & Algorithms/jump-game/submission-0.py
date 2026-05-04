class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            i+=nums[i]
            if nums[i]==nums[-1]:
                return True
        return False
        