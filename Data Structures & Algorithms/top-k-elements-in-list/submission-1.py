class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a={i:nums.count(i) for i in set(nums)}
        # u=list(a.keys())
        # u.sort(key=lambda x:a[x], reverse=True)
        # return u[:k]

        #using heap
        a={i:nums.count(i) for i in set(nums)}
        h=[]
        for val, freq in a.items():
            heapq.heappush(h, (freq, val))
            if len(h)>k:
                heapq.heappop(h)
        return [val for freq, val in h]



        