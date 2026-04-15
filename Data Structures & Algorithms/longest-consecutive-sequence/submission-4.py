class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First thought went to brute force where you look at each number and check their longest sequest starting with their number
        # Finally storing the max of longest length and current length
        my_set = set(nums)
        longest = 0
        if (len(nums)) == 0:
            return 0
        for i in range(len(nums)):
            cur, length = nums[i], 1
            while cur + 1 in my_set:
                length += 1
                cur = cur + 1
            longest = max(longest,length)
        return longest