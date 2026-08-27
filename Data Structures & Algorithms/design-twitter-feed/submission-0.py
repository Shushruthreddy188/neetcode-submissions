from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)   # userId -> [(time, tweetId)]
        self.followMap = defaultdict(set)   # userId -> set(followeeIds)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    maxHeap,
                    (time, tweetId, followeeId, index - 1)
                )

        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)

            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    maxHeap,
                    (time, tweetId, followeeId, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)