class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]

        for i in range(1, len(intervals)):
            last_added=res[-1]
            current=intervals[i]

            if current[0]<=last_added[1]:
                last_added[1]=max(last_added[1], current[1])
            else:
                res.append(current)

        return res






        