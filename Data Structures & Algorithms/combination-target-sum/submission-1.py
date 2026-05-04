class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(start, path, total):
            if total==target:
                res.append(path.copy())
                return
            if total>target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, path, total+nums[i])
                path.pop()
        
        dfs(0, [], 0)

        return res

        #I want to make a decision tree like approach, the first left take the first numner, second skip it, so in the first laeyer, we ha ve 2, 5, 6, 9
        #Then in the second followed by 2 with 2 and other will be 2 and 5 ans similarly, we can put a limit of target, and thus we can find the combination



        