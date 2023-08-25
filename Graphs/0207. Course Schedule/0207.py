class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) } # hashmap for each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # to determine cycles
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # if it did not catch false at any point in the loop (no cycle), it means that THAT course is actually able to be taken (no course cycle paradox)
            visitSet.remove(crs)
            preMap[crs] = []
            return True

