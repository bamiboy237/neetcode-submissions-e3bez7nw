from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = defaultdict(list)
        prereq_count = [0] * numCourses


        for course, prereq in prerequisites:
            dependents[prereq].append(course)
            prereq_count[course] += 1

        taking = deque([course for course in range(numCourses) if prereq_count[course] == 0])
        completed = 0

        while taking:
            course = taking.popleft()
            completed += 1
            for dependent in dependents[course]:
                prereq_count[dependent] -= 1
                if prereq_count[dependent] == 0:
                    taking.append(dependent)

        if completed == numCourses:
            return True
        return False