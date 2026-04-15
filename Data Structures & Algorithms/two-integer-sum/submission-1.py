class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in mem:
                return [mem[rem], i ]
            mem[nums[i]] = i
        
        