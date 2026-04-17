import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        # while stones:
        #     if len(stones)>=2:
        #         a=stones[-1]-stones[-2]
        #         stones.pop()
        #         stones.pop()
        #         stones.append(a)
        #         stones.sort()
        #     else:
        #         return stones[0]
        # return a

        max_heap=[-a for a in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            p=heapq.heappop(max_heap)
            q=heapq.heappop(max_heap)
            heapq.heappush(max_heap, p-q)
        return -max_heap[0] if max_heap else 0



        