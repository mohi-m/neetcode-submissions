class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * len(nums)
                continue
            prod = prod * num
        
        res = []

        for num in nums:
            if zero_count == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // num)
        
        return res