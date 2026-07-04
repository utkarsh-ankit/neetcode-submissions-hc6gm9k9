class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a={i:nums.count(i) for i in set(nums)}
        # u=list(a.keys())
        # u.sort(key=lambda x:a[x], reverse=True)
        # return u[:k]

        #using heap

        # a={i:nums.count(i) for i in set(nums)}
        # h=[]
        # for val, freq in a.items():
        #     heapq.heappush(h, (freq, val))
        #     if len(h)>k:
        #         heapq.heappop(h)
        # return [val for freq, val in h]

        #this is nlogk complexity

        #for O(n) complexity we use bucket sort

        l=[[] for _ in range(len(nums)+1)]
        res=[]

        dic=Counter(nums)

        for num,count in dic.items():
            l[count].append(num)

        for j in range(len(l)-1,-1,-1):
            if l[j]:
                res.extend(l[j])
            if len(res)==k:
                return res


        





        