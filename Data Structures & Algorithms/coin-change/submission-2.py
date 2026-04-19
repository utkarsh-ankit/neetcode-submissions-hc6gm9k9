class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def dfs(amount):
        #     if amount==0:
        #         return 0

        #     res=float('inf')

        #     for coin in coins:
        #         if amount-coin>=0:
        #             res=min(res, 1+dfs(amount-coin))
        #     return res

        # minc=dfs(amount)
        # return minc if minc != float('inf') else -1
#memo
        # memo={}

        # def dfs(amount):
        #     if amount==0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]

        #     res=float('inf')

        #     for coin in coins:
        #         if amount-coin>=0:
        #             res=min(res, 1+dfs(amount-coin))
            
        #     memo[amount] = res
        #     return res

        # minc=dfs(amount)
        # return minc if minc != float('inf') else -1
#iterative
        dp=[amount+1]*(amount+1)
        dp[0]=0

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1


