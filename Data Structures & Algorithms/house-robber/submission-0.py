class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        def dfs(i):
            if i>=n:
                return 0

            rob_now=nums[i]+dfs(i+2)
            rob_skip=dfs(i+1)

            return max(rob_now, rob_skip)
        return dfs(0)


        