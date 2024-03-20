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
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        ListNode* temp = list1;
        while (a-1) {
            temp = temp->next;
            a--;
            b--;
        }
        ListNode* temp2 = temp->next;
        while (b) {
            temp2 = temp2->next;
            b--;
        }

        temp->next = list2;
        
        ListNode* curr = list2;
        while (curr->next) {
            curr = curr->next;
        }
        curr->next = temp2;
        
        return list1;
    }
};