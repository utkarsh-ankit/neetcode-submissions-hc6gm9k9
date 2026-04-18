class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(r):
        #     if r==0:
        #         return 1
        #     if r<0:
        #         return 0
        #     return dfs(r-1)+dfs(r-2)
        # return dfs(n)

        memo={}
        def dfs(r):
            if r==0:
                return 1
            if r<0:
                return 0
            if r in memo:
                return memo[r]
            memo[r]=dfs(r-1)+dfs(r-2)
            return memo[r]

        return dfs(n)
        