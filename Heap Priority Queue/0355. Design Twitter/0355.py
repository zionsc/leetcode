class Twitter:

    def __init__(self):
        self.count = 0 # must decrement 0 --> float("-inf") because no maxHeap in python (more negative numbers will be first (most recent tweets))
        self.follower_map = defaultdict(set) # followerId : set(followeeIds)
        self.tweet_map = defaultdict(list) # userId : list(tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # add all all based on minHeap (reversed maxHeap into a res, then while it is less than 10 or minheap is not empty)
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)