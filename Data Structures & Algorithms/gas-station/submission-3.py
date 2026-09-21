class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]

            tank += net
            total += net

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1

        return start