class Solution:
    def rob(self, nums: List[int]) -> int:
        # n=len(nums)

        # def dfs(i):
        #     if i>=n:
        #         return 0

        #     rob_now=nums[i]+dfs(i+2)
        #     rob_skip=dfs(i+1)

        #     return max(rob_now, rob_skip)
        # return dfs(0)

#memo:-
        # n=len(nums)
        # memo={}

        # def dfs(i):
        #     if i>=n:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]

        #     memo[i]=nums[i]+dfs(i+2)
        #     memo[i+1]=dfs(i+1)

        #     return max(memo[i], memo[i+1])
        # return dfs(0)

#iterative:-
        rob1,rob2=0,0

        for n in nums:
            temp=max(n+rob1, rob2)
            rob1=rob2
            rob2=temp
        return rob2


        