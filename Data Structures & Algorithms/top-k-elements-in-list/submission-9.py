class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can also use min-heap to do this
        # First we count the frequency of each integer just like we did last time

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        # Now you create a min-heap of fixed size k and then you push all the num, freq pair to the heap and whenever the heap becomes 
        #larger than k, you pop until it becomes equal to k
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num ))
            if len(heap) > k:
                heapq.heappop(heap)
        
        #Now collect the result in an array and return it
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res