class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        

    def addNum(self, num: int) -> None:
        # -we can make two heaps, for first hald and second hald, if the 
        # first half is even and second too, we take the max and min of both
        # the halfs and then we find the mean
        # -if one of it is larger, we return that
        # -issue is, when we add something, how to know which heap it will go
        # and we also have to transer ferom on eheap to another if something is aadding up

        if self.large and num>self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small)>len(self.large)+1:
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large)>len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return float(-1*self.small[0])
        elif len(self.large)>len(self.small):
            return float(self.large[0])
        return (-1*self.small[0]+self.large[0])/2.0
    
        
        