class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        prev=float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0]<prev:
                count+=1
            else:
                prev=intervals[i][1]
        return count
