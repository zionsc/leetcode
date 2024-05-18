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
#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","lto","fast-math","march=native","omit-frame-pointer")
class Solution {
public:
    int distributeCoins(TreeNode* root) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        int res=0;
        dfs(root,res);
        return res;
    }
private:
    constexpr int dfs(TreeNode* node, int& res) {
        if(!node) return 0;
        int left=dfs(node->left,res);
        int right=dfs(node->right,res);
        res+=abs(left)+abs(right);
        return node->val+left+right-1;
    }
};