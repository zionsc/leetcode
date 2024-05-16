#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","lto","fast-math","march=native","omit-frame-pointer")
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
    bool evaluateTree(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        return dfs(root);
    }
private:
    bool dfs(TreeNode* node) {
        if(!node->left && !node->right){
            if(node->val==0) return false;
            if(node->val==1) return true;
        }
        bool left=dfs(node->left);
        bool right=dfs(node->right);
        if(node->val==2) return left || right;
        return left && right;
    }
};