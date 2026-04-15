class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Ofcourse there is a brute force method where you over the list 3 times and find the combinations
        # We sort the array just like before to avoid the duplicates.
        # To solve this problem using the concept of two sum what we need to do is break our problem into two sum. 
        # We add for loop on top of the our previous two sum algorith and find the combinations
        # Lets code this colution

        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i - 1] == nums[i]:
                continue 
                # This is to skip the duplicates as we would have same number at the first position as before
            # Find the deficit
            rem = 0 - nums[i]
            # Now lets implement the two sum
            fp = i + 1
            bp = len(nums) - 1
            while fp < bp:
                cur_sum = nums[fp] + nums[bp]
                if cur_sum == rem:
                    result.append([nums[i], nums[fp], nums[bp]])
                    fp += 1
                    bp -= 1
                    while nums[fp] == nums[fp - 1] and fp < bp:
                        fp += 1
                elif cur_sum > rem:
                    bp -= 1
                else:
                    fp += 1
                
        return result


