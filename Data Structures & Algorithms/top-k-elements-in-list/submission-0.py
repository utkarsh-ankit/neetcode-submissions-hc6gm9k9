class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={i:nums.count(i) for i in set(nums)}
        u=list(a.keys())
        u.sort(key=lambda x:a[x], reverse=True)
        return u[:k]


        