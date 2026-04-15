class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lets look at another solution which uses dynamic programming. Here instead of tracking just the maxProfit
        # You also track the minBuy for every index
        # At every iteration you update both the values by checking if the current profit (current index - minBuy ) is greater or not and also by checking 
        # If the minBuy is actually cheapest buy or not by comparing it to the current index

        minBuy = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)

        return maxProfit


        