class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for i in nums:
            if i in mem:
                return True
            else:
                mem[i] = 0
        return False
         