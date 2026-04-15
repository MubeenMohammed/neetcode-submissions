class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Lets try writing a brute force solution
        # Loop through the array twice and find the maxium element in the window. This might O(n^2) since there is a nested for loop
        if len(nums) == 0: return []
        l = 0
        r = k
        res = []
        while (r - 1) != len(nums):
            cur_max = -10000
            for i in range(l, r):
                cur_max = max(nums[i], cur_max)
            l += 1
            r += 1
            res.append(cur_max)
        return res




