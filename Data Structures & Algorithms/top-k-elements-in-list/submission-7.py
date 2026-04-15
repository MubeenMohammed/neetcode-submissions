class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        # Lets first get the freq of all the elemets
        freq_dict = {}
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i, 0)
        # Now lets use bucket sort to group the elements according to their frequency
        # First create an array with length len(nums) + 1 and default values of each element would be an empty array
        # Then group the elements according to their freq you get from the above
        # At the end return the top freq elements from the right
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in freq_dict.items():
            bucket[c].append(n)
        print(bucket)
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] == []:
                continue
            else:
                for j in bucket[i]:
                    if len(res) == k:
                        break
                    res.append(j)
        return res

        