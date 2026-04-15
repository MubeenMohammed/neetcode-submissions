class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorting Solution

        # First sort the array
        nums.sort()
        if len(nums) == 0:
            return 0
        count = 0
        temp = 1
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    continue
                if nums[i + 1] == nums[i] + 1:
                    temp += 1
                else:
                    temp = 1
            count = max(temp,count) 

        return count