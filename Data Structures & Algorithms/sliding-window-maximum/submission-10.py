class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # a=[]
        # for i in range(len(nums)-k+1):
        #     a.append(max(nums[i:i+k]))
        # return a

#heap
        # heap = []
        # output = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i >= k - 1:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

        o=[]
        q=deque()
        l=r=0

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                o.append(nums[q[0]])
                l+=1
            r+=1
        return o


        