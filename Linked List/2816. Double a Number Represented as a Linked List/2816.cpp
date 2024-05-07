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
    inline ListNode* doubleIt(ListNode* head) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        ListNode* prev=NULL;
        ListNode* curr=head;
        while(curr){
            ListNode* temp=curr->next;
            curr->next=prev;
            prev=curr;
            curr=temp;
        }

        int carry=0;
        ListNode* prev2=NULL;
        curr=prev;
        while(curr){
            int val=curr->val*2;
            val+=carry;
            curr->val=val%10;
            carry=val/10;
            prev2=curr;
            curr=curr->next;
        }

        if(carry){
            ListNode* newNode = new ListNode(carry);
            prev2->next=newNode;
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