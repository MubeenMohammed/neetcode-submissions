class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        # Get the product without considering zeros and also count number of zeros too
        result = []
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod = prod * i
        # If the zero count is more than 1 then solution is list of all zeros
        if zero_count > 1:
            return [0] * len(nums)
        
        # last two cases
        # Case 1: there is one zero: 
        # Case 2: There is no zeros -- This is simple as you have full prod just divide the prod with the current 
        # index value and add it to the result array
        
        for i,v in enumerate(nums):
            if zero_count == 1:
                if v == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(int(prod / v))

        return result