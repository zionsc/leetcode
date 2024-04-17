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
    vector<string>res;
    void dfs(TreeNode* node, string currString) {
        if(!node->left && !node->right){
            currString+=char(node->val+'a');
            reverse(currString.begin(),currString.end());
            res.push_back(currString);
            return;    
        }
        currString+=char(node->val+'a');
        if(node->left){
            dfs(node->left, currString);
        }
        if(node->right){
            dfs(node->right,currString);
        }
    }

    string smallestFromLeaf(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(!root){
            return "";
        }
        dfs(root,"");
        sort(res.begin(), res.end()); 
        return res[0];
    }
};