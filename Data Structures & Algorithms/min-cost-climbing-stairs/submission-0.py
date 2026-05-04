class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        def dfs(i):
            if i>=n:
                return 0
            
            one_step=dfs(i+1)
            two_step=dfs(i+2)

            return cost[i]+min(one_step, two_step)

        return min(dfs(0), dfs(1))
        