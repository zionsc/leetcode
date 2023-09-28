class Twitter:

    def __init__(self):
        self.count = 0 # must decrement 0 --> float("-inf") because no maxHeap in python (more negative numbers will be first (most recent tweets))
        self.follower_map = defaultdict(set) # followerId : set(followeeIds)
        self.tweet_map = defaultdict(list) # userId : list(count, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # add all all based on minHeap (reversed maxHeap into a res, then while it is less than 10 or minheap is not empty)
        res = []
        minHeap = []
        self.follower_map[userId].add(userId)
        for followeeId in self.follower_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index] # getting each count and tweetId (add each start of each followee into minHeap in order to iterate individually)
                heapq.heappush(minHeap, (count, followeeId, tweetId, index - 1))

        while minHeap and len(res) < 10:
            count, followeeId, tweetId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0: # now iterate the index for each userId (index - 1)
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(minHeap, (count, followeeId, tweetId, index - 1))
            
        return res
    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)