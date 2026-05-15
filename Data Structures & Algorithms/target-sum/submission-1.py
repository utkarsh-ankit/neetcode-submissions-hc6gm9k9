class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}

        def backtrack(i, total):
            if i==len(nums):
                return 1 if total==target else 0
            if (i, total) in dp:
                return dp[(i,total)]

            ways=backtrack(i+1, total+nums[i])+backtrack(i+1, total-nums[i])
            dp[i,total]=ways
            return ways

        return backtrack(0,0)

        