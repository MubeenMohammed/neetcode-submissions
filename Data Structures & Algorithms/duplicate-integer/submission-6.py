class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use sets to track the numbers and return the first time number is found twice

        visited = set()
        for i in nums:
            if i in visited:
                return True
            visited.add(i)
        return False

        
