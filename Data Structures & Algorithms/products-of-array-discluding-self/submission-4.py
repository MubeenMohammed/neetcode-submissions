class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        cur_prod = 1
        for i in range(len(nums)):
            prefix_prod[i] = cur_prod
            cur_prod *= nums[i]          
        cur_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix_prod[i] = cur_prod
            cur_prod *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(suffix_prod[i] * prefix_prod[i])
        return res
