class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # There is a challenge to complete this problem without using division
        # So we will use prefix and postfix  which is two arrays for each of the operation where it calculates 
        # the product of all the values before that index
        # For example the input is [1,2,4,6] so 
        # prefix for this will be [1, 1, 2, 8]
        # Similary for postfix it is the same thing but from the opposite side
        # Postfix for the above example will be [48,24,6,1]
        # Now to get the output all we need is to multiply both arrays values at their respective indices
        # Output is [48,24,12,8]
        # Even though this solution is optimal in terms of time complexity, it uses too much space so lets try to tackle that

        result = [1] * len(nums)
        # Lets do prefix on the result array it self
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        # Now lets calculate postfix and multiply to that index in the same array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):

            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result