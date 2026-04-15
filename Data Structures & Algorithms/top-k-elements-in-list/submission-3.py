class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem_dict = {}
        result = [[] for _ in range(len(nums) + 1)]
        final_result = []
        for i in nums:
            if i in mem_dict:
                mem_dict[i] += 1
            else:
                mem_dict[i] = 1
        for num, cnt in mem_dict.items():
            result[cnt].append(num)

        for i in range(len(result) - 1,0, -1):
            for num in result[i]:
                final_result.append(num)
                if len(final_result) == k:
                    return final_result
            
            