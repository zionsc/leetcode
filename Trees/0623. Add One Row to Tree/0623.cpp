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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(depth==1){
            TreeNode* newRoot=new TreeNode(val);
            newRoot->left=root;
            return newRoot;
        }

        deque<pair<TreeNode*,int>>q;
        q.push_back({root,1});

        while(!q.empty()){
            TreeNode* curr=q.front().first;
            int level=q.front().second;
            q.pop_front();
            if(level==depth-1){
                q.push_front({curr,level});
                break;
            }
            if(curr->left){
                q.push_back({curr->left,level+1});
            }
            if(curr->right){
                q.push_back({curr->right,level+1});
            }
        }
        
        for(auto p : q){
            auto curr=p.first;
            auto level=p.second;
            if(curr->left){
                TreeNode* temp=curr->left;
                TreeNode* newNode=new TreeNode(val);
                curr->left=newNode;
                newNode->left=temp;
            } else{
                TreeNode* newNode=new TreeNode(val);
                curr->left=newNode;
            }
            if(curr->right){
                TreeNode* temp2=curr->right;
                TreeNode* nextNode=new TreeNode(val);
                curr->right=nextNode;
                nextNode->right=temp2;
            } else{
                TreeNode* nextNode=new TreeNode(val);
                curr->right=nextNode;
            }
        }
        return root;
        

    }
};