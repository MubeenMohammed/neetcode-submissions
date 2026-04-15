class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use sets to track the numbers and return the first time number is found twice

        mem = set()
        for i in nums:
            if i in mem:
                return True
            else:
                mem.add(i)
        return False