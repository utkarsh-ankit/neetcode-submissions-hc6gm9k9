class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        m = 0
        count = 0
        end = 0
        for i in range(len(nums) - 1):
            m = max(m, i + nums[i])
            if i == end:
                count += 1
                end = m
        return count
