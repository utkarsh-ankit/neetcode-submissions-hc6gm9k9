class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        ss=[]

        def dfs(i):
            if i>=len(nums):
                res.add(tuple(ss))
                return
            ss.append(nums[i])
            dfs(i+1)
            ss.pop()
            dfs(i+1)

        dfs(0)
        return [list(x) for x in res]