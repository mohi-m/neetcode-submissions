class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_map = defaultdict(list)
        for idx, num in enumerate(nums):
            lookup_map[num].append(idx)
        
        for idx, num in enumerate(nums):
            diff = target - num
            if lookup_map[diff] and idx != lookup_map[diff][0]:
                return [min(idx, lookup_map[diff][0]), max(idx, lookup_map[diff][0])]
        
        return []
