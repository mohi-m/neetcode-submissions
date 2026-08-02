class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_map = {}
        for idx, num in enumerate(nums):
            lookup_map[num]= idx
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in lookup_map and idx != lookup_map[diff]:
                return [idx, lookup_map[diff]]
        
        return []
