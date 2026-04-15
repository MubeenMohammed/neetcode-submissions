class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Intialize the hashmap to check the numbers
        num_dict = {}

        for i in nums:
            if i in num_dict:
                return True
            else:
                num_dict[i] = 1
        return False
        