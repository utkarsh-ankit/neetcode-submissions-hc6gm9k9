class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # res=set()
        # ss=[]

        # def dfs(i):
        #     if i>=len(nums):
        #         res.add(tuple(ss))
        #         return
        #     ss.append(nums[i])
        #     dfs(i+1)
        #     ss.pop()
        #     dfs(i+1)

        # dfs(0)
        # return [list(x) for x in res]

        nums.sort()
        res=[]

        def backtrack(i, subset):
            if i==len(nums):
                res.append(subset[::]) #same as subset.copy()
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1

            backtrack(i+1, subset)

        backtrack(0,[])

        return res