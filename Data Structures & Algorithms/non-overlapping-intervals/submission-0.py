class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        maxRight = intervals[0][1]
        minRemove = 0
        for i,j in intervals[1:]:
            print(f'i: {i}, j: {j}')
            if i < maxRight:
                print('remove condition')
                minRemove += 1
                maxRight = min(j, maxRight)
            else:
                maxRight = j
        
        return minRemove
            
            