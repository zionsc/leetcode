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
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        unordered_map<int, ListNode*> sumAllocation;
        int prefix = 0;
        sumAllocation[prefix] = dummy;

        while (head) {
            prefix += head->val;
            sumAllocation[prefix] = head;
            head = head->next;
        }

        prefix = 0;
        head = dummy;

        while (head) {
            prefix += head->val;      
            head->next = sumAllocation[prefix]->next;
            head = head->next;
        }

        return dummy->next;
    }
}