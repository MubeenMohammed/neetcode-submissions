class Solution:
    def trap(self, height: List[int]) -> int:
        # Basically You can solve this problem in two ways one using O(n) time and O(n) memory 
        # Another way to solve this problem is using same time complexity but O(1) memory using two pointer
        # Lets look at the first solution

        # Go through the array and calculate the current index right max height and left max height
        # Then calculate the min of those two max 
        # To get the current index capacity, you can just do min(leftMax, rightMax) - curIndex

        # Now lets try two pointer solution to avoid excess use of memory

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
