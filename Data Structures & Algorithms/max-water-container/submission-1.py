class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Lets try a fluke using two pointer solution. 
        # Now what I am thinking is there are two pointers one at the front of the list and one at the back
        # You calculate the area and save it in a variable.
        # Now you compare both heights and check which height is less
        # If front pointer height is less then move it to one right and 
        # Similary if the back pointer height is less then move it to one left and calculate the area and keep the max area

        # Lets code this fluke solution

        fp = 0
        bp = len(heights) - 1
        result = 0

        while fp < bp:
            area = min(heights[fp], heights[bp]) * (bp - fp)
            result = max(result, area)
            if heights[fp] < heights[bp]:
                fp += 1
            else:
                bp -= 1
        return result