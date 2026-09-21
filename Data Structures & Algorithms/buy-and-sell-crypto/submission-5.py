class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        best_profit = 0
        lowest_buy = prices[0]

        for price in prices[1:]:
            if price <= lowest_buy:
                lowest_buy = price
            else:
                best_profit = max(best_profit, price - lowest_buy)

        return best_profit