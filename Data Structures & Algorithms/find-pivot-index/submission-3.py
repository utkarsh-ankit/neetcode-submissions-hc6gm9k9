class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)-nums[0]

        for i in range(len(nums)):
            if left==right:
                return i
            left=left+nums[i]
            if i + 1 < len(nums):
                right=right-nums[i+1]
        return -1


        