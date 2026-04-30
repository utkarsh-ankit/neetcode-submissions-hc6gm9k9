class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c={i:nums.count(i) for i in nums}
        for i,v in c.items():
            if v==1:
                return i
        