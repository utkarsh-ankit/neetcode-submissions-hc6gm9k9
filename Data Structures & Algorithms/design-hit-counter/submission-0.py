class HitCounter:

    def __init__(self):
        self.hits_map={}
        
    def hit(self, timestamp: int) -> None:
        idx=timestamp%300

        if idx in self.hits_map and self.hits_map[idx][0]==timestamp:
            time,count=self.hits_map[idx]
            self.hits_map[idx]=(time,count+1)
        else:
            self.hits_map[idx]=(timestamp,1)
        

    def getHits(self, timestamp: int) -> int:
        total_hits=0

        for stored_time, stored_count in self.hits_map.values():
            if timestamp-stored_time<300:
                total_hits+=stored_count

        return total_hits
        

#what I am thinking is that we can make a ditonary that have 1-300 range, anything that will be added in dictiory after 300 timesteps, will be minused from 300 an s will be added in the dictory, , but the adding will be done a list, to pop if any value exists if it is older than the time range of 300

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
