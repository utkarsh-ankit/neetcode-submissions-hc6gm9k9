class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr_sum=float('-inf')

        for n in nums:
            curr_sum=max(curr_sum, 0)
            curr_sum+=n
            max_sum=max(curr_sum,n)

        return curr_sum
        