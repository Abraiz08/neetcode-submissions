class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        l = 0
        r = min(1, len(prices) - 1)
        if l == r:
            return 0
        while r <= (len(prices)-1):
            profit = prices[r] - prices[l]
            maxprice = max(maxprice, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxprice
            


            