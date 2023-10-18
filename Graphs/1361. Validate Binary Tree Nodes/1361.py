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
        # 3. all nodes are visited
    