/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int result = 0;
        DFS(root, result);
        return result;

    }
private: 
    int DFS(TreeNode* root, int& result) {
        if (root == NULL) {
            return 0;
        }

        int left = DFS(root->left, result);
        int right = DFS(root->right, result);

        result = max(result, left + right);
        return 1 + max(left, right);
    }
};