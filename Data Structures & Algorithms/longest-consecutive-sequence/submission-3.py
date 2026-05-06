class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seqeunce = set(nums)
        if not nums:
            return 0

        max_count = 1
        for i in seqeunce:
            count = 1
            if i-1 not in seqeunce:
                while i+1 in seqeunce:
                    count += 1
                    max_count = max(max_count, count)
                    i = i+1
        
        return max_count
            
