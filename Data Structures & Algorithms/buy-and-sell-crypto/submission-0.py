class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First lets try to write a brute force solution by iterating through the array twice. The time complexity is
        # O(n) and memory is O(1)

        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res,prices[j] - prices[i])

        return res