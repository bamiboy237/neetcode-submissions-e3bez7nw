class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_prev_cost = cost[0]
        prev_cost = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev_cost, prev_prev_cost)
            prev_prev_cost = prev_cost
            prev_cost = curr

        return min(prev_cost, prev_prev_cost)