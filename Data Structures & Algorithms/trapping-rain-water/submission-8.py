class Solution:
    def trap(self, height: List[int]) -> int:
        # Basically You can solve this problem in two ways one using O(n) time and O(n) memory 
        # Another way to solve this problem is using same time complexity but O(1) memory using two pointer
        # Lets look at the first solution

        # Go through the array and calculate the current index right max height and left max height
        # Then calculate the min of those two max 
        # To get the current index capacity, you can just do min(leftMax, rightMax) - curIndex

        leftMax = []
        currentLeftMax = 0
        for i in height:
            currentLeftMax = max(i, currentLeftMax)
            leftMax.append(currentLeftMax)
        
        rightMax = [0] * len(height)
        currentRightMax = 0
        for i in range(len(height) - 1, -1, -1):
            currentRightMax = max(height[i], currentRightMax)
            rightMax[i] = currentRightMax

        
        res = 0
        for i in range(len(height)):
            area = min(leftMax[i], rightMax[i]) - height[i]
            if (area > 0):
                res += area
        return res