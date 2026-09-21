class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fuel = start = 0

        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
            else:
                continue
        return start