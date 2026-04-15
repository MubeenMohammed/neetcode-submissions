class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Okay lets solve this problem in brute force which I think should be simple enough
        result = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                # Calculate the area of the rectangle
                # Get the minimum of two heights and that will be the height of the container
                ch = min(heights[i], heights[j])
                cw = j - i
                area = ch * cw
                result = max(result,area)

        return result