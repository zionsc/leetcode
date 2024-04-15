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
    vector<int>res;
    void dfs(TreeNode* node) {
        if(!node){
            return;
        }
        if(node->left && !node->right){
            res.push_back(node->left->val);
        }
        if(!node->left && node->right){
            res.push_back(node->right->val);
        }
        dfs(node->left);
        dfs(node->right);
    }
    vector<int> getLonelyNodes(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        dfs(root);
        return res;
    }
};