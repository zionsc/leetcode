class Twitter:

    def __init__(self):
        self.count = 0
        self.follower_map = defaultdict(set) # followerId : set(followeeIds)
        self.tweet_map = defaultdict(list) # userId : list(tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # add all all based on minHeap (reversed maxHeap into a res, )
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)