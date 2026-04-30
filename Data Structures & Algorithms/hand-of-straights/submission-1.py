class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False


        hmap={}
        for i in hand:
            hmap[i]=hmap.get(i,0)+1
        
        minH=list(hmap.keys())
        heapq.heapify(minH)

        while minH:
            first=minH[0]

            for i in range(first, first+groupSize):
                if i not in hmap: #check if the next smallest (consequtive(+1)) present there
                    return False
                hmap[i]-=1

                if hmap[i]==0:
                    #we now fist check if middle value count is already ended before the smallest one
                    if i!=minH[0]:
                        return False

                    heapq.heappop(minH)
        return True

