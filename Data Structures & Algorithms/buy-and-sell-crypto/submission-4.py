class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            cash = max(cash, hold + price)
            hold = max(hold, -price)

        return cash