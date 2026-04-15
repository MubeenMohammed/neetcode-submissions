class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in memory:
                return [memory[rem], i]
            memory[nums[i]] = i
        