class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=float("-inf")
        current=0

        for i in range(len(nums)):
            current+=nums[i]
            summ=max(summ, current)
            if current<0:
                current=0

        return summ


        