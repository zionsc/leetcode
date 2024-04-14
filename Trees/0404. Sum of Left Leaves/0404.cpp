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

 #pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int dfs(TreeNode* node){
        if(!node){
            return 0;
        }
        int sm = dfs(node->left) + dfs(node->right);
        if(node->left && !node->left->left && !node->left->right){
            sm+=node->left->val;
        }
        return sm;
    }

    int sumOfLeftLeaves(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        return dfs(root);
    }
};