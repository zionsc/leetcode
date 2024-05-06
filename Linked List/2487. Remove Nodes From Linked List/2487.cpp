/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#pragma GCC optimize('03','unroll-loops')
class Solution {
public:
    inline ListNode* removeNodes(ListNode* head) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        ListNode* curr=head;
        ListNode* prev=NULL;
        while(curr){
            ListNode* temp=curr->next;
            curr->next=prev;
            prev=curr;
            curr=temp;
        }

        curr=prev;
        while(curr){
            while(curr->next && curr->val>curr->next->val){
                curr->next=curr->next->next;
            }
            curr=curr->next;
        }

        curr=prev;
        prev=NULL;
        while(curr){
            ListNode* temp=curr->next;
            curr->next=prev;
            prev=curr;
            curr=temp;
        }

        return prev;
    }
};