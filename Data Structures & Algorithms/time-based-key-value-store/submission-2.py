class TimeMap:

    def __init__(self):
        self.TimeMap={}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key]=[]
        self.TimeMap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        else:
            v=self.TimeMap[key]
            l=0
            r=len(v)-1
            result=""
            while l<=r:
                mid=(l+r)//2
                if v[mid][1]<=timestamp:
                    result = v[mid][0]
                    l=mid+1
                if v[mid][1]>timestamp:
                    r=mid-1
            return result
        
