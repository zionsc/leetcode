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
#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(!root) return NULL;

        if(!root->left && !root->right && root->val==target){
            return NULL;
        }
        
        root->left=removeLeafNodes(root->left,target);
        root->right=removeLeafNodes(root->right,target);

        if(!root->left && !root->right && root->val==target) return NULL;
        return root;
    }
};