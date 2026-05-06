class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        prefix = 1
        
        for i, num in enumerate(nums):
            output[i] = prefix
            prefix = prefix * num

        suffix = 1

        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * suffix
            suffix *= nums[i]
        
        return output