class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}

        def dfs(i):
            if i>=n:
                return 0
            
            if i in memo:
                return memo[i]

            memo[i]=nums[i]+dfs(i+2)
            memo[i+1]=dfs(i+1)

            return max(memo[i], memo[i+1])
        return dfs(0)


        