/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#pragma GCC optimize('03')

class Solution {
public:
    inline void deleteNode(ListNode* node) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        *node=*node->next;
    }
};