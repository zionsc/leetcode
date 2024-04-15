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
    int dfs(TreeNode* node, int currNum) {
        if(!node->left && !node->right){
            return node->val + currNum;
        }
        int res=0;
        if(node->left){
            res+=dfs(node->left, (node->val+currNum)*10);
        }
        if(node->right){
            res+=dfs(node->right, (node->val+currNum)*10);
        }
        return res;
    }

    int sumNumbers(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        return dfs(root, 0);
    }
};