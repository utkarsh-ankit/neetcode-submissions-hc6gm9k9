class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v=float("inf")
        max_d=float("-inf")

        for i in prices:
            min_v=min(min_v,i)
            max_d=max(max_d,i-min_v)

        return max_d
        