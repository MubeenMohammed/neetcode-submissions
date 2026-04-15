class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = {}
        for i in nums:
            if i in memory:
                return True
            memory[i] = 0
        return False
         