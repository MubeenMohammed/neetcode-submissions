class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lets try the two pointer with sliding window approach. 
        # The idea is simple. We have two pointers. Initially, left pointer at 0 and right pointer at 1 and then see if
        #  if the right pointer is greater than the left pointer. 
            # If it is then calculate the profit and see if it is greater than the current profit and also increase the right pointer by 1 so that you calculate every max profit with that current min buy
            # If right is less than or equal to the left then move the left pointer to where right pointer is and move the right pointer by 1

        # Lets code up the solution

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(prices[r] - prices[l], res)
            r += 1
        return res

        