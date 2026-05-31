"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x: (x.start, x.end))
        ends = []
        rooms = 0
        for interval in intervals:
            st = interval.start
            end = interval.end
            ends = [e for e in ends if e > st] + [end]
            rooms = max(rooms, len(ends))
        return rooms























        # count=0
        # res=0
        # start=sorted(i.start for i in intervals)
        # end=sorted(i.end for i in intervals)

        # s,e=0,0

        # while s<len(intervals):
        #     if start[s]<end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e+=1
        #         count-=1
        #     res=max(res, count)
        # return res
            






        