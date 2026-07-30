class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for curs, pre in prerequisites:
            preMap[curs].append(pre)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if preMap[node] == []:
                return True
            visited.add(node)
            for pre in preMap[node]:
                if not dfs(pre):return False
            visited.remove(node)
            preMap[node] = []
            return True
        # this loop for not fully connected graph
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True