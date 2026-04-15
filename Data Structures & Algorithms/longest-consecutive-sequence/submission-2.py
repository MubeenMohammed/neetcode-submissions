class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # So the idea is to convert the array into a set and then iterate through the array
        # We are now trying to find different sequence length and every sequence has a starting point
        # So we go through the array and see if the current number is the start of the sequence or not
        # How do we check that? we do num - 1 not in set (finding if there any numbers in the sequence left of the current number )
        # If it is the start of the sequence then do while loop and find the sequence length
        # If its not the start of the sequence then skip the number
        # Finally find the length of longest sequence

        # Lets write the code for this above solution
        # Convert the array into a set
        my_set = set(nums)
        longest = 0
        for i in nums:
            length = 0
            if i - 1 not in my_set:
                cur = i
                length = 1
                while cur + 1 in my_set:
                    length += 1
                    cur += 1
                longest = max(longest, length) 
        return longest
