class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        # 1. create adj_list
        adj_list = { i:[] for i in range(n) }
        for i in range(n):
            if leftChild[i] != -1:
                adj_list[i].append(leftChild[i])
            if rightChild[i] != -1:
                adj_list[i].append(rightChild[i])

        # 2. all nodes have one parent other than root
        parentCount = { i:0 for i in range(n) }
        for i in range(n):
            for child in adj_list[i]:
                parentCount[child] += 1
                if parentCount[child] > 1:
                    return False
            rootCount = sum(1 for i in parentCount if parentCount[i] != 1)
            if rootCount != 1:
                return False

        # 3. all nodes are visited
        visited = set()
        def dfs(node):
            visited.add(node)
            for child in adj_list[node]:
                dfs(child)
        dfs(next(i for i, count in parentCount.items() if count == 0))
        
        return True if len(visited) == n else False
    