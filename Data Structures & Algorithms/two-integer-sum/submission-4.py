class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mem:
                return [mem[diff], i]
            mem[nums[i]] = i
        