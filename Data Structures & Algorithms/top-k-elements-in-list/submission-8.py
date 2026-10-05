class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Can we do this using a hashmap
        # What if I calculate the frequency of each integer and then store them in an hashmap
        # Then loop until k and remove top k elements based on frequency from the hashmap

        mem = {}
        for i in nums:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        # Here you use sorting to get the k most frequent elements
        arr = []
        for num, cnt in mem.items():
           arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res 