class MedianFinder:

    def __init__(self):
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        tmp = self.minheap[:]
        n = len(tmp)

        if n%2 == 0:
            first = 0
            for i in range(n//2):
                first = heapq.heappop(tmp)
            second = heapq.heappop(tmp)
            return (first + second) / 2
        else:
            first = 0
            for i in range(n//2 + 1):
                first = heapq.heappop(tmp)
            return first