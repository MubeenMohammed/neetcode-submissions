
        # Lets implement binary search. 
        # So the idea here is you loop through every number and find the deficit i.e. target - current number
        # And you find that deficit using binary search from i + 1 and len(array)

        # So Lets code this solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []



