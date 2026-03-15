#Course Schedule
# Time complexity ->  O(E+V) basically the edges (prerequisites) and the v is courses
# Space complexity -> O(E+V) basically the edges (prerequisites) and the v is courses

# Logic -> Find indegree which is nothing just an array representation of how many courses course i is dependent on. Then
# starting one with the 0 indegree courses keep updating the iorder for child courses. If indegree of each course is now
# 0 means possible else not possible
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        dependencyMap = {}
        coursesTaken = 0

        for course, dependentOn in prerequisites:
            indegree[course] +=1
            if dependentOn in dependencyMap:
                dependencyMap[dependentOn].append(course)
            else:
                dependencyMap[dependentOn] = [course]

        # found all the courses with no dependencies
        coursesThatCanBeTaken = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                coursesTaken+=1
                coursesThatCanBeTaken.append(i)

        if len(coursesThatCanBeTaken) == 0 :
            return False

        if coursesTaken == numCourses:
            return True

        while len(coursesThatCanBeTaken) > 0:
            course = coursesThatCanBeTaken.popleft()
            if course in dependencyMap:
                for dependentCr in  dependencyMap[course]:
                    indegree[dependentCr] -= 1
                    if indegree[dependentCr] == 0:
                        coursesTaken+=1
                        coursesThatCanBeTaken.append(dependentCr)
                        if coursesTaken == numCourses:
                            return True
        
        return coursesTaken == numCourses