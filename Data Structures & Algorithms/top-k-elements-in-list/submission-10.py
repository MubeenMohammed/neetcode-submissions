class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Third and most optimal solution is using array of fixed length which is k 
        # And we know that there wont be a element whose frequency would be greater than k
        # Each index in this array is frequency group, you put all the elements with that frequency at that index
        # Eg: 2 has a frequency of 2 then you store 2 at index 2
        #Finally you return k elements from the frequency indexed array

        #First just like before, you get the frequency of all the elements

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        # Here you create an array with fixed length of k (+ 1 is to offset the values by 1 since index start at 0 and we will count the frequency from 1)
        fia = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            fia[cnt].append(num)
        
        #Now you return the k elements from right to left since we need top k frequent elements
        res = []
        for i in range(len(fia) - 1, 0, -1):
            for num in fia[i]:
                res.append(num)
                if len(res) == k:
                    return res