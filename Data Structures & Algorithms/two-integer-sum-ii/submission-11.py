class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Okay now the most efficient solution that meets all the requirements
        # Two pointer solution where there ofcourse two pointers, 
        # First we point front pointer to the start of the list and back pointer to the end of the list
        # Add those numbers at that position and see the difference
        # If the difference is 0 then we found our indices 
        # If the target is smaller than the sum we found then move the right pointer one to the left
        # And if the target is bigger than the sum we found then move the left pointer one to the right until we find our two magic numbers

        fp = 0
        bp = len(numbers) - 1
        while fp < bp:
            cur_sum = numbers[fp] + numbers[bp]
            if cur_sum == target:
                return [fp + 1, bp + 1]
            elif cur_sum > target:
                bp -= 1
            else:
                fp += 1
        return []
