class Twitter:

    def __init__(self):
        self.count=0
        self.tm=defaultdict(list)
        self.fm=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tm[userId].append([self.count, tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        
        mh=[]

        self.fm[userId].add(userId)
        for followeeId in self.fm[userId]:
            if followeeId in self.tm and len(self.tm[followeeId]) > 0:
                index=len(self.tm[followeeId])-1
                count, tweetId=self.tm[followeeId][index]
                heapq.heappush(mh, [count,tweetId, followeeId, index-1])

        while mh and len(res)<10:
            count, tweetId, followeeId, index=heapq.heappop(mh)
            res.append(tweetId)
            if index>=0:
                count, tweetId=self.tm[followeeId][index]
                heapq.heappush(mh, [count, tweetId, followeeId, index-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fm[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fm[followerId]:
            self.fm[followerId].remove(followeeId)
