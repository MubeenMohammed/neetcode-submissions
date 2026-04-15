class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Lets implement binary search. 
        # So the idea here is you loop through every number and find the deficit i.e. target - current number
        # And you find that deficit using binary search from i + 1 and len(array)

        # So Lets code this solution
        for i in range(len(numbers)):
            deficit = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = (l + r)// 2
                if deficit == numbers[mid]:
                    return [i + 1, mid + 1]
                if numbers[mid] > deficit:
                    r = mid - 1
                else:
                    l = mid + 1
        return []



