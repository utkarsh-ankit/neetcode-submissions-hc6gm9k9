class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursion
        # def dfs(i,j):
        #     if i == (m-1) and j==(n-1):
        #         return 1
        #     if i >=m or j>=n:
        #         return 0
        #     return dfs(i,j+1)+ dfs(i+1, j)
        # return dfs(0,0)

        #memo
        # memo=[[-1]*n for _ in range(m)] #2D grid
        # def dfs(i,j):
        #     if i==(m-1) and j==(n-1):
        #         return 1
        #     if i>=m or j>=n:
        #         return 0
        #     if memo[i][j]!=-1:
        #         return memo[i][j]
        #     memo[i][j]=dfs(i, j+1)+ dfs(i+1,j)
        #     return memo[i][j]
        # return dfs(0,0)

        #iterative (the idea of value function in RL)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1]=1 #making boundary 1 because only down and rignt is allowed
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]+=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]


