class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) } # hashmap for each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()

        