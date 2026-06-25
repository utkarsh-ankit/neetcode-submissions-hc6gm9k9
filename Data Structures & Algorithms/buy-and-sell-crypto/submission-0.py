class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p=float("inf")
        diff=float("-inf")

        for i in prices:
            min_p=min(min_p,i)
            diff=max(diff,(i-min_p))
        
        return diff
        