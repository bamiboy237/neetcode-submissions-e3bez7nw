class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True, key = lambda x: x[0])

        for car in cars:
            fleets.append((target - car[0]) / car[1])
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets) 